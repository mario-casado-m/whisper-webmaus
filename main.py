from asr import ASR
from webmaus import WebMAUS

if __name__ == "__main__":
    asr = ASR(model="large")
    transcripcion = asr.transcribe('', lang='spanish')
    WebMAUS(audiopath='', text=transcripcion, lang='spa-ES')
