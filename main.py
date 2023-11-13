from os import path

BASE = "https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/"

class WebMAUS(object):
    def __init__(self, filename, lang):
        self.filename = filename
        self.lang = lang
        self.run_maus_basic()

    def dl_maus_res(self, link):
        from requests import get

        res = get(link)

        if res.status_code == 200:
            with open(path.join('input', self.filename + ".TextGrid"), 'w') as w:
                w.write(res.text)
        else:
            raise Exception(res.text)

    def process_maus_res(self, res):
        import xml.etree.ElementTree as ET

        tree = ET.fromstring(res)
        link = tree.find('downloadLink').text

        if link != None:
            self.dl_maus_res(link)
        else:
            raise Exception(tree.find('output').text)

    def run_maus_basic(self):
        from requests import post

        service_name = "runMAUSBasic"
        URL = BASE + "/" + service_name
        audio = self.filename + ".wav"
        txt = self.filename + ".txt"

        files = {
            'SIGNAL': (audio, open(path.join('input', audio), 'rb'), 'audio/x-wav'),
            'TEXT': (txt, open(path.join('input', txt), encoding='utf-8').read(), 'text/txt'),
            'LANGUAGE': (None, self.lang)
        }

        res = post(URL,files=files)

        if res.status_code == 200:
            self.process_maus_res(res.text)
        else:
            raise Exception(res.text)

if __name__ == "__main__":
    WebMAUS(filename='', lang='spa-ES')
