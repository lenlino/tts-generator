import voiceroid2


def generate_wav(voice, text):
    software = voice.SOFTWARE_NAME
    if software == "VOICEROID2":
        return voiceroid2.generate_wav(text, voice.SYSTEM_NAME)