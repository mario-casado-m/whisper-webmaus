# Script para un pipeline Whisper -> WebMAUS
Con estos scripts se puede realizar la transcripción de un audio utilizando [Whisper](https://github.com/openai/whisper) y generar el TextGrid correspondiente mediante la API de [WebMAUS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface).

# Set up
Se recomienda utilizar un entorno virtual. La lista de dependencias está disponible tanto en el archivo `requirements.txt` como en el `Pipfile`.

La librería Whisper requiere tener en el PATH del sistema operativo [`ffmpeg`](https://www.ffmpeg.org/). Si no está disponible, el módulo de Whisper no funcionará.

# Funcionamiento
Este script consta de dos módulos. El primero (`asr.py`) realiza la transcripción de audio utilizando Whisper. Para comenzar a utlizarlo, primero hay que inicializar el objeto `ASR()`, que cargará el modelo de lenguaje. Podemos incluir como argumento el [tamaño de modelo](https://github.com/openai/whisper#available-models-and-languages) que deseemos. Si no indicamos ningún tamaño, cargará el más pequeño (`tiny`).

``` python
from asr import ASR

asr = ASR(model="large")
```

Si se van a procesar varios audios, **solo hay que inicializar el modelo una vez** al principio del script. Una vez hecho, se puede usar para transcribir tantas veces como sea neceario (p. ej., en un bucle.)

Una vez inicializado el objeto `ASR()` podemos usar el método `transcribe()` para realizar la transcripción de un audio. Debemos indicar en primer lugar, la ruta al audio que queremos transcribir y, en segundo lugar, la lengua en la que deseamos generar la transcripción de entre [todos aquellos de los que dispone Whisper](https://github.com/openai/whisper/blob/fcfeaf1b61994c071bba62da47d7846933576ac9/whisper/tokenizer.py#L10):

``` python
transcripcion = asr.transcribe('C:\ruta\a\mi\audio.wav', lang='spanish')
```

La función `transcribe()` devuelve la transcripción como cadena de texto (`str()`). Esta transcripción podríamos escribirla en un archivo o, si lo deseamos, mandarla al segundo módulo de este script (`webmaus.py`).

El módulo WebMAUS conecta con la API del servicio WebMAUS para crear un TextGrid a partir de un audio y su transcripción. Para poder utilizar sus funciones, primero debemos instaciarlo:

``` python
from webmaus import WebMAUS

maus = WebMAUS()
```

A continuación, podemos usar una de las dos funciones disponibles (`run_maus_basic` y `run_pipeline`). `run_maus_basic` traerá como resultado un TextGrid con un tier de palabras y otro de segmentos. `run_pipeline` está configurado para el *pipeline* `G2P_MAUS_PHO2SYL`, que añade silabificación.

Solo debemos indicar la ruta al archivo, el texto la transcripción y la lengua en la debe operar el servicio de entre [aquellas que acepta](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface).

``` python
from webmaus import WebMAUS

maus.run_maus_basic((audiopath='C:\ruta\a\mi\audio.wav', text=transcripcion, lang='spa-ES')
```

Con esa sentencia, el módulo `webmaus.py` se encargará de solicitar la creación del TextGrid al servicio online y crear el archivo correspondiente en el mismo directorio en el que esté el audio.

El archivo `main.py` contiene la secuencia de sentencias mencionadas para la ejecución. 

# Licencia
Este script ha sido creado por [Mario Casado-Mancebo](https://www.mcasado.org) y se publica bajo una licencia MIT.
