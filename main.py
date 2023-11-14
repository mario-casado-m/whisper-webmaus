from asr import ASR
from webmaus import WebMAUS

if __name__ == "__main__":
    audiopath = ''
    asr = ASR(model="large")
    transcripcion = asr.transcribe(audiopath, lang='spanish')
    maus = WebMAUS()
    maus.run_maus_basic(audiopath=audiopath, text=transcripcion, lang='spa-ES')
