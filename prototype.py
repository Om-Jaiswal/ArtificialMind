from audio2text import Recognizer
from text2audio import Converter
from translate import Translate

r = Recognizer()
c = Converter()
translator = Translate()

def main():
    audio_lang = 'ml-IN'        # 
    trans_lang = 'hin_Deva'     # tam_Taml, tel_Telu, mal_Mlyn
    c_lang = 'hi'               # Bengali: bn, English : en, Gujarati: gu, Hindi: hi
    filename = 'new.wav'
    transcript = r.transcribe("test_malayalam.wav", lang=audio_lang)
    translated = translator.translate(transcript, trans_lang)
    c.convert(translated, lang=trans_lang, filename=filename)


