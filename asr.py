import whisper

class ASR(object):
    def __init__(self, model="tiny"):
        print('Cargando modelo...')
        '''
        Lo primero es cargar el modelo.
        Decidimos el tamaño (tiny, base, small, medium, large). Cuanto más grande, más preciso, pero también más pesado y más tiempo de carga y procesamiento.
        Solo tenemos que cargarlo una vez. Por eso, lo hacemos al principio del script y FUER DEL BUCLE
        '''
        self.model = whisper.load_model(model)
        print('Modelo cargado.')

    def transcribe(self, filepath, lang):
        from os import path

        '''
        Definimos la lengua en la que queremos nuestras transcripciones
        Todas las lenguas disponibles en whisper están en este enlace:
          https://github.com/openai/whisper/blob/fcfeaf1b61994c071bba62da47d7846933576ac9/whisper/tokenizer.py#L10
        '''
        LANGUAGE = lang

        print(f'Generando transcripcion...')

        '''
        generamos la transcripción con Whisper pasandole el nombre de archivo que creamos antes
        con el argumento language forzamos la lengua de la transcripción
        '''
        transcription = self.model.transcribe(filepath, language=LANGUAGE)

        return transcription['text']
