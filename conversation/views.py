import contextlib
from django.shortcuts import render, redirect
from conversation.models import Room, Message
from django.http import HttpResponse, JsonResponse
from translate import Translate

LANGUAGE = ''
ROOMNAME = ''
LANGUAGES = {}
translator = Translate()

lang2code = {"Acehnese (Arabic script)" : "ace_Arab" , "Acehnese (Latin script)" : "ace_Latn" , 
            "Mesopotamian Arabic" : "acm_Arab" , "Ta’izzi-Adeni Arabic" : "acq_Arab" , 
            "Tunisian Arabic" : "aeb_Arab" , "Afrikaans" : "afr_Latn" , "South Levantine Arabic" : "ajp_Arab" , 
            "Akan" : "aka_Latn" , "Amharic" : "amh_Ethi" , "North Levantine Arabic" : "apc_Arab" , 
            "Modern Standard Arabic" : "arb_Arab" , "Modern Standard Arabic (Romanized)" : "arb_Latn" , 
            "Najdi Arabic" : "ars_Arab" , "Moroccan Arabic" : "ary_Arab" , "Egyptian Arabic" : "arz_Arab" , 
            "Assamese" : "asm_Beng" , "Asturian" : "ast_Latn" , "Awadhi" : "awa_Deva" , "Central Aymara" : "ayr_Latn" , 
            "South Azerbaijani" : "azb_Arab" , "North Azerbaijani" : "azj_Latn" , "Bashkir" : "bak_Cyrl" , 
            "Bambara" : "bam_Latn" , "Balinese" : "ban_Latn" , "Belarusian" : "bel_Cyrl" , "Bemba" : "bem_Latn" , "Bengali" : "ben_Beng" , "Bhojpuri" : "bho_Deva" , "Banjar (Arabic script)" : "bjn_Arab" , "Banjar (Latin script)" : "bjn_Latn" , "Standard Tibetan" : "bod_Tibt" , "Bosnian" : "bos_Latn" , "Buginese" : "bug_Latn" , "Bulgarian" : "bul_Cyrl" , "Catalan" : "cat_Latn" , "Cebuano" : "ceb_Latn" , "Czech" : "ces_Latn" , "Chokwe" : "cjk_Latn" , "Central Kurdish" : "ckb_Arab" , "Crimean Tatar" : "crh_Latn" , "Welsh" : "cym_Latn" , "Danish" : "dan_Latn" , "German" : "deu_Latn" , "Southwestern Dinka" : "dik_Latn" , "Dyula" : "dyu_Latn" , "Dzongkha" : "dzo_Tibt" , "Greek" : "ell_Grek" , "English" : "eng_Latn" , "Esperanto" : "epo_Latn" , "Estonian" : "est_Latn" , "Basque" : "eus_Latn" , "Ewe" : "ewe_Latn" , "Faroese" : "fao_Latn" , "Fijian" : "fij_Latn" , "Finnish" : "fin_Latn" , "Fon" : "fon_Latn" , "French" : "fra_Latn" , "Friulian" : "fur_Latn" , "Nigerian Fulfulde" : "fuv_Latn" , "Scottish Gaelic" : "gla_Latn" , "Irish" : "gle_Latn" , "Galician" : "glg_Latn" , "Guarani" : "grn_Latn" , "Gujarati" : "guj_Gujr" , "Haitian Creole" : "hat_Latn" , "Hausa" : "hau_Latn" , "Hebrew" : "heb_Hebr" , "Hindi" : "hin_Deva" , "Chhattisgarhi" : "hne_Deva" , "Croatian" : "hrv_Latn" , "Hungarian" : "hun_Latn" , "Armenian" : "hye_Armn" , "Igbo" : "ibo_Latn" , "Ilocano" : "ilo_Latn" , "Indonesian" : "ind_Latn" , "Icelandic" : "isl_Latn" , "Italian" : "ita_Latn" , "Javanese" : "jav_Latn" , "Japanese" : "jpn_Jpan" , "Kabyle" : "kab_Latn" , "Jingpho" : "kac_Latn" , "Kamba" : "kam_Latn" , "Kannada" : "kan_Knda" , "Kashmiri (Arabic script)" : "kas_Arab" , "Kashmiri (Devanagari script)" : "kas_Deva" , "Georgian" : "kat_Geor" , "Central Kanuri (Arabic script)" : "knc_Arab" , "Central Kanuri (Latin script)" : "knc_Latn" , "Kazakh" : "kaz_Cyrl" , "Kabiyè" : "kbp_Latn" , "Kabuverdianu" : "kea_Latn" , "Khmer" : "khm_Khmr" , "Kikuyu" : "kik_Latn" , "Kinyarwanda" : "kin_Latn" , "Kyrgyz" : "kir_Cyrl" , "Kimbundu" : "kmb_Latn" , "Northern Kurdish" : "kmr_Latn" , "Kikongo" : "kon_Latn" , "Korean" : "kor_Hang" , "Lao" : "lao_Laoo" , "Ligurian" : "lij_Latn" , "Limburgish" : "lim_Latn" , "Lingala" : "lin_Latn" , "Lithuanian" : "lit_Latn" , "Lombard" : "lmo_Latn" , "Latgalian" : "ltg_Latn" , "Luxembourgish" : "ltz_Latn" , "Luba-Kasai" : "lua_Latn" , "Ganda" : "lug_Latn" , "Luo" : "luo_Latn" , "Mizo" : "lus_Latn" , "Standard Latvian" : "lvs_Latn" , "Magahi" : "mag_Deva" , "Maithili" : "mai_Deva" , "Malayalam" : "mal_Mlym" , "Marathi" : "mar_Deva" , "Minangkabau (Arabic script)" : "min_Arab" , "Minangkabau (Latin script)" : "min_Latn" , "Macedonian" : "mkd_Cyrl" , "Plateau Malagasy" : "plt_Latn" , "Maltese" : "mlt_Latn" , "Meitei (Bengali script)" : "mni_Beng" , "Halh Mongolian" : "khk_Cyrl" , "Mossi" : "mos_Latn" , "Maori" : "mri_Latn" , "Burmese" : "mya_Mymr" , "Dutch" : "nld_Latn" , "Norwegian Nynorsk" : "nno_Latn" , "Norwegian Bokmål" : "nob_Latn" , "Nepali" : "npi_Deva" , "Northern Sotho" : "nso_Latn" , "Nuer" : "nus_Latn" , "Nyanja" : "nya_Latn" , "Occitan" : "oci_Latn" , "West Central Oromo" : "gaz_Latn" , "Odia" : "ory_Orya" , "Pangasinan" : "pag_Latn" , "Eastern Panjabi" : "pan_Guru" , "Papiamento" : "pap_Latn" , "Western Persian" : "pes_Arab" , "Polish" : "pol_Latn" , "Portuguese" : "por_Latn" , "Dari" : "prs_Arab" , "Southern Pashto" : "pbt_Arab" , "Ayacucho Quechua" : "quy_Latn" , "Romanian" : "ron_Latn" , "Rundi" : "run_Latn" , "Russian" : "rus_Cyrl" , "Sango" : "sag_Latn" , "Sanskrit" : "san_Deva" , "Santali" : "sat_Olck" , "Sicilian" : "scn_Latn" , "Shan" : "shn_Mymr" , "Sinhala" : "sin_Sinh" , "Slovak" : "slk_Latn" , "Slovenian" : "slv_Latn" , "Samoan" : "smo_Latn" , "Shona" : "sna_Latn" , "Sindhi" : "snd_Arab" , "Somali" : "som_Latn" , "Southern Sotho" : "sot_Latn" , "Spanish" : "spa_Latn" , "Tosk Albanian" : "als_Latn" , "Sardinian" : "srd_Latn" , "Serbian" : "srp_Cyrl" , "Swati" : "ssw_Latn" , "Sundanese" : "sun_Latn" , "Swedish" : "swe_Latn" , "Swahili" : "swh_Latn" , "Silesian" : "szl_Latn" , "Tamil" : "tam_Taml" , "Tatar" : "tat_Cyrl" , "Telugu" : "tel_Telu" , "Tajik" : "tgk_Cyrl" , "Tagalog" : "tgl_Latn" , "Thai" : "tha_Thai" , "Tigrinya" : "tir_Ethi" , "Tamasheq (Latin script)" : "taq_Latn" , "Tamasheq (Tifinagh script)" : "taq_Tfng" , "Tok Pisin" : "tpi_Latn" , "Tswana" : "tsn_Latn" , "Tsonga" : "tso_Latn" , "Turkmen" : "tuk_Latn" , "Tumbuka" : "tum_Latn" , "Turkish" : "tur_Latn" , "Twi" : "twi_Latn" , "Central Atlas Tamazight" : "tzm_Tfng" , "Uyghur" : "uig_Arab" , "Ukrainian" : "ukr_Cyrl" , "Umbundu" : "umb_Latn" , "Urdu" : "urd_Arab" , "Northern Uzbek" : "uzn_Latn" , "Venetian" : "vec_Latn" , "Vietnamese" : "vie_Latn" , "Waray" : "war_Latn" , "Wolof" : "wol_Latn" , "Xhosa" : "xho_Latn" , "Eastern Yiddish" : "ydd_Hebr" , "Yoruba" : "yor_Latn" , "Yue Chinese" : "yue_Hant" , "Chinese (Simplified)" : "zho_Hans" , "Chinese (Traditional)" : "zho_Hant" , "Standard Malay" : "zsm_Latn" , "Zulu" : "zul_Latn"}

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
    global ROOMNAME
    LANGUAGE = request.POST['language']
    ROOMNAME = room
    if LANGUAGES.get(ROOMNAME, 0):
        LANGUAGES[ROOMNAME].append(LANGUAGE)
    else:
        LANGUAGES[ROOMNAME] = []
        LANGUAGES[ROOMNAME].append(LANGUAGE)
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
    room_name = ROOMNAME
    room_id = request.POST['room_id']
    print('---'*20, room_name) 

    langs_in_room = LANGUAGES[room_name]

    new_message = ''
    for lang in langs_in_room:
        new_message = new_message + "<br>" + translator.translate(message, lang=lang2code[lang])

    new_message = Message.objects.create(value=new_message, user=username, lang=language, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})