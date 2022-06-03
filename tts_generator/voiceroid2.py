import threading

import pyvcroid2
import winsound


def generate_wav(text, voicename):
    with pyvcroid2.VcRoid2() as vc:
        # Load language library
        lang_list = vc.listLanguages()
        if "standard" in lang_list:
            vc.loadLanguage("standard")
        elif 0 < len(lang_list):
            vc.loadLanguage(lang_list[0])
        else:
            raise Exception("No language library")

        # Load Voice
        voice_list = vc.listVoices()
        if 0 < len(voice_list):
            vc.loadVoice(voicename)
        else:
            raise Exception("No voice library")

        print(voicename)

        # Set parameters
        vc.param.volume = 1.23
        vc.param.speed = 0.987
        vc.param.pitch = 1.111
        vc.param.emphasis = 0.893
        vc.param.pauseMiddle = 80
        vc.param.pauseLong = 100
        vc.param.pauseSentence = 200
        vc.param.masterVolume = 1.123

        # Text to speech
        speech, tts_events = vc.textToSpeech(text)

        filename = "./generate/"+text+".wav"
        with open(filename, mode="wb") as f:
            f.write(speech)
        return filename
