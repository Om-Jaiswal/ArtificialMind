import contextlib
from django.shortcuts import render, redirect
from conversation.models import Room, Message
from django.http import HttpResponse, JsonResponse

LANGUAGE = ''

# Create your views here.
def conversation(request):
    context = {
        "lang_list" : sorted([
            "Acehnese (Arabic script)","Acehnese (Latin script)","Mesopotamian Arabic","Ta’izzi-Adeni Arabic","Tunisian Arabic","Afrikaans","South Levantine Arabic","Akan","Amharic","North Levantine Arabic",
            "Modern Standard Arabic","Modern Standard Arabic (Romanized)","Najdi Arabic","Moroccan Arabic","Egyptian Arabic","Assamese","Asturian","Awadhi","Central Aymara","South Azerbaijani","North Azerbaijani",
            "Bashkir","Bambara","Balinese","Belarusian","Bemba","Bengali","Bhojpuri","Banjar (Arabic script)","Banjar (Latin script)","Standard Tibetan","Bosnian","Buginese","Bulgarian","Catalan","Cebuano","Czech",
            "Chokwe","Central Kurdish","Crimean Tatar","Welsh","Danish","German","Southwestern Dinka","Dyula","Dzongkha","Greek","English","Esperanto","Estonian","Basque","Ewe","Faroese","Fijian","Finnish","Fon",
            "French","Friulian","Nigerian Fulfulde","Scottish Gaelic","Irish","Galician","Guarani","Gujarati","Haitian Creole","Hausa","Hebrew","Hindi","Chhattisgarhi","Croatian","Hungarian","Armenian","Igbo",
            "Ilocano","Indonesian","Icelandic","Italian","Javanese","Japanese","Kabyle","Jingpho","Kamba","Kannada","Kashmiri (Arabic script)","Kashmiri (Devanagari script)","Georgian","Central Kanuri (Arabic script)",
            "Central Kanuri (Latin script)","Kazakh","Kabiyè","Kabuverdianu","Khmer","Kikuyu","Kinyarwanda","Kyrgyz","Kimbundu","Northern Kurdish","Kikongo","Korean","Lao","Ligurian","Limburgish","Lingala","Lithuanian",
            "Lombard","Latgalian","Luxembourgish","Luba-Kasai","Ganda","Luo","Mizo","Standard Latvian","Magahi","Maithili","Malayalam","Marathi","Minangkabau (Arabic script)","Minangkabau (Latin script)","Macedonian",
            "Plateau Malagasy","Maltese","Meitei (Bengali script)","Halh Mongolian","Mossi","Maori","Burmese","Dutch","Norwegian Nynorsk","Norwegian Bokmål","Nepali","Northern Sotho","Nuer","Nyanja","Occitan",
            "West Central Oromo","Odia","Pangasinan","Eastern Panjabi","Papiamento","Western Persian","Polish","Portuguese","Dari","Southern Pashto","Ayacucho Quechua","Romanian","Rundi","Russian","Sango","Sanskrit",
            "Santali","Sicilian","Shan","Sinhala","Slovak","Slovenian","Samoan","Shona","Sindhi","Somali","Southern Sotho","Spanish","Tosk Albanian","Sardinian","Serbian","Swati","Sundanese","Swedish","Swahili",
            "Silesian","Tamil","Tatar","Telugu","Tajik","Tagalog","Thai","Tigrinya","Tamasheq (Latin script)","Tamasheq (Tifinagh script)","Tok Pisin","Tswana","Tsonga","Turkmen","Tumbuka","Turkish","Twi",
            "Central Atlas Tamazight","Uyghur","Ukrainian","Umbundu","Urdu","Northern Uzbek","Venetian","Vietnamese","Waray","Wolof","Xhosa","Eastern Yiddish","Yoruba","Yue Chinese","Chinese (Simplified)",
            "Chinese (Traditional)","Standard Malay","Zulu"
        ])
    }
    return render(request, 'conversation/conversation.html', context)

def room(request, room):
    username = request.GET.get('username')
    language = request.GET.get('language')
    room_details = Room.objects.get(name=room)
    return render(request, 'conversation/room.html', {
        'username': username,
        'language': language,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    global LANGUAGE 
    LANGUAGE = request.POST['language']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    language = LANGUAGE
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, lang=language, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})