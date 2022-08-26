from django.shortcuts import render
from .models import MultipleAudio
from audio2text import Recognizer
from text2audio import Converter
from translate import Translate

r = Recognizer()
c = Converter()
translator = Translate()


l2c = {'Afrikaans': 'af', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Bengali': 'bn', 'Bosnian': 'bs', 'Catalan': 'ca', 'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'German': 'de', 'Greek': 'el', 'English': 'en', 'Esperanto': 'eo', 'Spanish': 'es', 'Estonian': 'et', 'Finnish': 'fi', 'French': 'fr', 'Gujarati': 'gu', 'Hindi': 'hi', 'Croatian': 'hr', 'Hungarian': 'hu', 'Armenian': 'hy', 'Indonesian': 'id', 'Icelandic': 'is', 'Italian': 'it', 'Hebrew': 'iw', 'Japanese': 'ja', 'Javanese': 'jw', 'Khmer': 'km', 'Kannada': 'kn', 'Korean': 'ko', 'Latin': 'la', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malay': 'ms', 'Malayalam': 'ml', 'Marathi': 'mr', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Dutch': 'nl', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Sinhala': 'si', 'Slovak': 'sk', 'Albanian': 'sq', 'Serbian': 'sr', 'Sundanese': 'su', 'Swedish': 'sv', 'Swahili': 'sw', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Filipino': 'tl', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Vietnamese': 'vi', 'Chinese': 'zh-CN', 'Chinese (Mandarin/Taiwan)': 'zh-TW', 'Chinese (Mandarin)': 'zh'}
languages = ["Afrikaans", "Arabic", "Bulgarian", "Bengali", "Bosnian", "Catalan", "Czech", "Welsh", "Danish", "German", "Greek", "English", "Esperanto", "Spanish", "Estonian", "Finnish", "French", "Gujarati", "Hindi", "Croatian", "Hungarian", "Armenian", "Indonesian", "Icelandic", "Italian", "Hebrew", "Japanese", "Javanese", "Khmer", "Kannada", "Korean", "Latin", "Latvian", "Macedonian", "Malay", "Malayalam", "Marathi", "Myanmar (Burmese)", "Nepali", "Dutch", "Norwegian", "Polish", "Portuguese", "Romanian", "Russian", "Sinhala", "Slovak", "Albanian", "Serbian", "Sundanese", "Swedish", "Swahili", "Tamil", "Telugu", "Thai", "Filipino", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Chinese", "Chinese (Mandarin/Taiwan)", "Chinese (Mandarin)"]


# Create your views here.
def upload(request):

    if request.method == "POST":
        audio = request.FILES.getlist('audio')
        for audio in audios:
            MultipleAudio.objects.create(audio=audio)  

    audios = MultipleAudio.objects.all()

    try:
        i_lang = request.POST['ilanguage']
        t_lang = request.POST['tlanguage']

        print('**'*10, i_lang, t_lang, '**'*10)
        aud_path = audios[len(audios)-1].audios.url

        text = r.transcribe(aud_path, lang='ml-IN')
        
        translated = translator.translate(text, lang=l2c[t_lang])

        c.convert(translated, lang=t_lang, filename='new.wav')
    except:
        i_lang = ''
        t_lang = ''

        translated = ''
    
    context = {
        "ocr_languages" : sorted(languages),
        "translation_languages" : sorted(languages),
        "image": audios,
        "translation": 'new.wav'
    }
    return render(request, 'audioconvert/audioconvert.html', context)