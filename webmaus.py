from os import path

BASE = "https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/"

class WebMAUS(object):

    def set_vars(self, audiopath, text, lang):
        self.audio = audiopath
        self.filename = path.basename(self.audio).rstrip(".wav")
        self.folder = path.dirname(self.audio)
        self.text = text
        self.lang = lang

    def create_basic_dict(self):
        '''funcion que crea un diccionario con los tres elementos basicos de cualquier peticion a WebMAUS: el audio, la transcripcion y el lenguaje'''
        audio = self.filename + ".wav"
        txt = self.filename + ".txt"

        return {
            'SIGNAL': (audio, open(self.audio, 'rb'), 'audio/x-wav'),
            'TEXT': (txt, self.text, 'text/txt'),
            'LANGUAGE': (None, self.lang)
        }

    def send_maus(self, url, files):
        '''funcion que envia la peticion con los datos a la API de WebMAUS'''
        from requests import post

        res = post(url, files=files)

        if res.status_code == 200:
            self.process_maus_res(res.text)
        else:
            raise Exception(res.text)

    def dl_maus_res(self, link):
        '''funcion que descarga el TextGrid que devuelve WebMAUS'''
        from requests import get

        res = get(link)

        if res.status_code == 200:
            with open(path.join(self.folder, self.filename + ".TextGrid"), 'w') as w:
                w.write(res.text)
        else:
            raise Exception(res.text)

    def process_maus_res(self, res):
        '''funcion que procesa la respuesta de la API de WebMAUS y, si hay error, devuelve una excepcion'''
        import xml.etree.ElementTree as ET

        tree = ET.fromstring(res)
        link = tree.find('downloadLink').text

        if link != None:
            self.dl_maus_res(link)
        else:
            raise Exception(tree.find('output').text)

    def run_maus_basic(self, audiopath, text, lang):
        '''peticion de un servicio basico a WebMAUS: una transcripcion de fonemas y palabras'''
        service_name = "runMAUSBasic"
        url = BASE + "/" + service_name

        self.set_vars(audiopath, text, lang)

        files = self.create_basic_dict()

        self.send_maus(url, files)

    def run_pipeline(self, audiopath, text, lang):
        '''peticion compleja a WebMAUS: fonemas, silabas, palabras y ortografico'''
        service_name = "runPipeline"
        url = BASE + "/" + service_name

        self.set_vars(audiopath, text, lang)

        files = self.create_basic_dict()
        files.update(
            {
                'PIPE': (None, "G2P_MAUS_PHO2SYL")
            }
        )

        self.send_maus(url, files)
