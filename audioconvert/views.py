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
lang2code = {"Acehnese (Arabic script)" : "ace_Arab" , "Acehnese (Latin script)" : "ace_Latn" , 
            "Mesopotamian Arabic" : "acm_Arab" , "Ta’izzi-Adeni Arabic" : "acq_Arab" , 
            "Tunisian Arabic" : "aeb_Arab" , "Afrikaans" : "afr_Latn" , "South Levantine Arabic" : "ajp_Arab" , 
            "Akan" : "aka_Latn" , "Amharic" : "amh_Ethi" , "North Levantine Arabic" : "apc_Arab" , 
            "Modern Standard Arabic" : "arb_Arab" , "Modern Standard Arabic (Romanized)" : "arb_Latn" , 
            "Najdi Arabic" : "ars_Arab" , "Moroccan Arabic" : "ary_Arab" , "Egyptian Arabic" : "arz_Arab" , 
            "Assamese" : "asm_Beng" , "Asturian" : "ast_Latn" , "Awadhi" : "awa_Deva" , "Central Aymara" : "ayr_Latn" , 
            "South Azerbaijani" : "azb_Arab" , "North Azerbaijani" : "azj_Latn" , "Bashkir" : "bak_Cyrl" , 
            "Bambara" : "bam_Latn" , "Balinese" : "ban_Latn" , "Belarusian" : "bel_Cyrl" , "Bemba" : "bem_Latn" , "Bengali" : "ben_Beng" , "Bhojpuri" : "bho_Deva" , "Banjar (Arabic script)" : "bjn_Arab" , "Banjar (Latin script)" : "bjn_Latn" , "Standard Tibetan" : "bod_Tibt" , "Bosnian" : "bos_Latn" , "Buginese" : "bug_Latn" , "Bulgarian" : "bul_Cyrl" , "Catalan" : "cat_Latn" , "Cebuano" : "ceb_Latn" , "Czech" : "ces_Latn" , "Chokwe" : "cjk_Latn" , "Central Kurdish" : "ckb_Arab" , "Crimean Tatar" : "crh_Latn" , "Welsh" : "cym_Latn" , "Danish" : "dan_Latn" , "German" : "deu_Latn" , "Southwestern Dinka" : "dik_Latn" , "Dyula" : "dyu_Latn" , "Dzongkha" : "dzo_Tibt" , "Greek" : "ell_Grek" , "English" : "eng_Latn" , "Esperanto" : "epo_Latn" , "Estonian" : "est_Latn" , "Basque" : "eus_Latn" , "Ewe" : "ewe_Latn" , "Faroese" : "fao_Latn" , "Fijian" : "fij_Latn" , "Finnish" : "fin_Latn" , "Fon" : "fon_Latn" , "French" : "fra_Latn" , "Friulian" : "fur_Latn" , "Nigerian Fulfulde" : "fuv_Latn" , "Scottish Gaelic" : "gla_Latn" , "Irish" : "gle_Latn" , "Galician" : "glg_Latn" , "Guarani" : "grn_Latn" , "Gujarati" : "guj_Gujr" , "Haitian Creole" : "hat_Latn" , "Hausa" : "hau_Latn" , "Hebrew" : "heb_Hebr" , "Hindi" : "hin_Deva" , "Chhattisgarhi" : "hne_Deva" , "Croatian" : "hrv_Latn" , "Hungarian" : "hun_Latn" , "Armenian" : "hye_Armn" , "Igbo" : "ibo_Latn" , "Ilocano" : "ilo_Latn" , "Indonesian" : "ind_Latn" , "Icelandic" : "isl_Latn" , "Italian" : "ita_Latn" , "Javanese" : "jav_Latn" , "Japanese" : "jpn_Jpan" , "Kabyle" : "kab_Latn" , "Jingpho" : "kac_Latn" , "Kamba" : "kam_Latn" , "Kannada" : "kan_Knda" , "Kashmiri (Arabic script)" : "kas_Arab" , "Kashmiri (Devanagari script)" : "kas_Deva" , "Georgian" : "kat_Geor" , "Central Kanuri (Arabic script)" : "knc_Arab" , "Central Kanuri (Latin script)" : "knc_Latn" , "Kazakh" : "kaz_Cyrl" , "Kabiyè" : "kbp_Latn" , "Kabuverdianu" : "kea_Latn" , "Khmer" : "khm_Khmr" , "Kikuyu" : "kik_Latn" , "Kinyarwanda" : "kin_Latn" , "Kyrgyz" : "kir_Cyrl" , "Kimbundu" : "kmb_Latn" , "Northern Kurdish" : "kmr_Latn" , "Kikongo" : "kon_Latn" , "Korean" : "kor_Hang" , "Lao" : "lao_Laoo" , "Ligurian" : "lij_Latn" , "Limburgish" : "lim_Latn" , "Lingala" : "lin_Latn" , "Lithuanian" : "lit_Latn" , "Lombard" : "lmo_Latn" , "Latgalian" : "ltg_Latn" , "Luxembourgish" : "ltz_Latn" , "Luba-Kasai" : "lua_Latn" , "Ganda" : "lug_Latn" , "Luo" : "luo_Latn" , "Mizo" : "lus_Latn" , "Standard Latvian" : "lvs_Latn" , "Magahi" : "mag_Deva" , "Maithili" : "mai_Deva" , "Malayalam" : "mal_Mlym" , "Marathi" : "mar_Deva" , "Minangkabau (Arabic script)" : "min_Arab" , "Minangkabau (Latin script)" : "min_Latn" , "Macedonian" : "mkd_Cyrl" , "Plateau Malagasy" : "plt_Latn" , "Maltese" : "mlt_Latn" , "Meitei (Bengali script)" : "mni_Beng" , "Halh Mongolian" : "khk_Cyrl" , "Mossi" : "mos_Latn" , "Maori" : "mri_Latn" , "Burmese" : "mya_Mymr" , "Dutch" : "nld_Latn" , "Norwegian Nynorsk" : "nno_Latn" , "Norwegian Bokmål" : "nob_Latn" , "Nepali" : "npi_Deva" , "Northern Sotho" : "nso_Latn" , "Nuer" : "nus_Latn" , "Nyanja" : "nya_Latn" , "Occitan" : "oci_Latn" , "West Central Oromo" : "gaz_Latn" , "Odia" : "ory_Orya" , "Pangasinan" : "pag_Latn" , "Eastern Panjabi" : "pan_Guru" , "Papiamento" : "pap_Latn" , "Western Persian" : "pes_Arab" , "Polish" : "pol_Latn" , "Portuguese" : "por_Latn" , "Dari" : "prs_Arab" , "Southern Pashto" : "pbt_Arab" , "Ayacucho Quechua" : "quy_Latn" , "Romanian" : "ron_Latn" , "Rundi" : "run_Latn" , "Russian" : "rus_Cyrl" , "Sango" : "sag_Latn" , "Sanskrit" : "san_Deva" , "Santali" : "sat_Olck" , "Sicilian" : "scn_Latn" , "Shan" : "shn_Mymr" , "Sinhala" : "sin_Sinh" , "Slovak" : "slk_Latn" , "Slovenian" : "slv_Latn" , "Samoan" : "smo_Latn" , "Shona" : "sna_Latn" , "Sindhi" : "snd_Arab" , "Somali" : "som_Latn" , "Southern Sotho" : "sot_Latn" , "Spanish" : "spa_Latn" , "Tosk Albanian" : "als_Latn" , "Sardinian" : "srd_Latn" , "Serbian" : "srp_Cyrl" , "Swati" : "ssw_Latn" , "Sundanese" : "sun_Latn" , "Swedish" : "swe_Latn" , "Swahili" : "swh_Latn" , "Silesian" : "szl_Latn" , "Tamil" : "tam_Taml" , "Tatar" : "tat_Cyrl" , "Telugu" : "tel_Telu" , "Tajik" : "tgk_Cyrl" , "Tagalog" : "tgl_Latn" , "Thai" : "tha_Thai" , "Tigrinya" : "tir_Ethi" , "Tamasheq (Latin script)" : "taq_Latn" , "Tamasheq (Tifinagh script)" : "taq_Tfng" , "Tok Pisin" : "tpi_Latn" , "Tswana" : "tsn_Latn" , "Tsonga" : "tso_Latn" , "Turkmen" : "tuk_Latn" , "Tumbuka" : "tum_Latn" , "Turkish" : "tur_Latn" , "Twi" : "twi_Latn" , "Central Atlas Tamazight" : "tzm_Tfng" , "Uyghur" : "uig_Arab" , "Ukrainian" : "ukr_Cyrl" , "Umbundu" : "umb_Latn" , "Urdu" : "urd_Arab" , "Northern Uzbek" : "uzn_Latn" , "Venetian" : "vec_Latn" , "Vietnamese" : "vie_Latn" , "Waray" : "war_Latn" , "Wolof" : "wol_Latn" , "Xhosa" : "xho_Latn" , "Eastern Yiddish" : "ydd_Hebr" , "Yoruba" : "yor_Latn" , "Yue Chinese" : "yue_Hant" , "Chinese (Simplified)" : "zho_Hans" , "Chinese (Traditional)" : "zho_Hant" , "Standard Malay" : "zsm_Latn" , "Zulu" : "zul_Latn"}
la2co = {'Hindi': 'hi-IN', 'Tamil': 'ta-IN', 'Telugu': 'te-IN', 'Malayalam': 'ml-IN'}

# Create your views here.
def upload(request):

    if request.method == "POST":
        audios = request.FILES.getlist('audios')
        for audio in audios:
            MultipleAudio.objects.create(audios=audio)  

    audios = MultipleAudio.objects.all()

    try:
        i_lang = request.POST['ilanguage']
        t_lang = request.POST['tlanguage']

        print('**'*10, i_lang, t_lang, '**'*10)
        aud_path = audios[len(audios)-1].audios.url

        text = r.transcribe(aud_path, lang=l2c[i_lang])
        
        translated = translator.translate(text, lang=lang2code[t_lang])

        c.convert(translated, lang=la2co[t_lang], filename='new.wav')
    except:
        i_lang = ''
        t_lang = ''

        translated = ''
    
    context = {
        "ocr_languages" : sorted(languages),
        "translation_languages" : sorted(languages),
        "audio": audios,
        "translation": 'new.wav'
    }
    return render(request, 'audioconvert/audioconvert.html', context)