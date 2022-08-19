from gtts import gTTS

# {'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan',
# 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'eo': 'Esperanto',
# 'es': 'Spanish', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'hi': 'Hindi',
# 'hr': 'Croatian', 'hu': 'Hungarian', 'hy': 'Armenian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian',
# 'iw': 'Hebrew', 'ja': 'Japanese', 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin',
# 'lv': 'Latvian', 'mk': 'Macedonian', 'ms': 'Malay', 'ml': 'Malayalam', 'mr': 'Marathi', 'my': 'Myanmar (Burmese)',
# 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
# 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese',
# 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish',
# 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-CN': 'Chinese', 'zh-TW': 'Chinese (Mandarin/Taiwan)',
# 'zh': 'Chinese (Mandarin)'}

class Converter:
    def __init__(self, ):
        pass

    def convert(self, text, lang='en', filename=''):
        tts = gTTS(text, lang=lang)
        if filename:
            tts.save(filename)


def main():
    conv = Converter()
    conv.convert('ආයුබෝවන් ඔබට කොහොමද අද දවස', lang='si', filename='test_sinhala.wav')


if __name__ == "__main__":
    main()

    
