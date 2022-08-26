const URL = "https://teachablemachine.withgoogle.com/models/_zjVBdiwg/";
let model, webcam, ctx, labelContainer, maxPredictions;

async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";

  model = await tmPose.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();

  const size = 350;
  const flip = true;
  webcam = new tmPose.Webcam(350, size, flip);
  await webcam.setup();
  await webcam.play();
  window.requestAnimationFrame(loop);

  const canvas = document.getElementById("canvas");
  canvas.width = size; canvas.height = size;
  ctx = canvas.getContext("2d");
  labelContainer = document.getElementById("label-container");
  for (let i = 0; i < maxPredictions; i++) {
    labelContainer.appendChild(document.createElement("div"));
  }
}

async function loop(timestamp) {
  webcam.update();
  await predict();
  window.requestAnimationFrame(loop);
}

async function predict() {
  const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
  const prediction = await model.predict(posenetOutput);
//  let maximum = 0
//  for (let i = 0; i < maxPredictions; i++) {
//      labelContainer.childNodes[i].innerHTML = " "
//  }
const translation = {'Assamese': ['হ্যালো',
'হেই,',
'কি হৈছে',
'মোৰ নাম',
'মই চিনাকি ভাষা শিকোঁ',
'তোমাৰ নাম কি?',
"তুমি ক'ৰ পৰা আছা?",
'তুমি কেনে আছা?',
'ধন্যবাদ'],
'Awadhi': ['हैलो.',
'अरे, ऊ का',
'का होई',
'मोर नाउँ अहइ',
'मैं साइन लैंग्वेज सीख रहा हु',
'तोहार नाउँ का अहइ?',
'तू कहाँ स आवा अहा?',
'अउर तू का करत अहा?',
'.. धन्यवाद फिर से'],
'Bengali': ['হ্যালো.',
'হেই, হেই।',
'কি হচ্ছে?',
'আমার নাম',
'আমি সাইন ল্যাঙ্গুয়েজ শিখছি',
'তোমার নাম কি?',
'তুমি কোথা থেকে এসেছ?',
'তুমি কেমন আছো?',
'ধন্যবাদ'],
'Bhojpuri': ['बा बा बा',
'अरे, आपन.',
'का हो गइल बा?',
'मोर नाँव',
'हम सियाही भाषा सीख रहल बानी',
'तोहार नाँव का बा?',
'तू कहाँ के बाटे?',
'कइसे हो गइल?',
'धन्यवाद बा.'],
'English': ["Hello","Hey","What's Up", "My Name", "I am Learning Sign Language", 
"What's your name?", "Where are you from?", "How are you?", "Thank You"],
'Gujarati': ['હેલો',
'હેય',
'શું છે',
'મારું નામ',
'હું સાઇન લેંગ્વેજ શીખી રહ્યો છું',
'તમારું નામ શું છે?',
'તમે ક્યાંથી છો?',
'તમે કેવી રીતે છો?',
'આભાર'],
'Hindi': ['नमस्ते',
'हैलो',
'क्या है',
'मेरा नाम',
'मैं साइन लैंग्वेज सीख रहा हूँ',
'तुम्हारा नाम क्या है?',
'तुम कहाँ से हो?',
'आप कैसे हैं?',
'धन्यवाद'],
'Chhattisgarhi': ['हेलो',
'हे हे',
'का होही',
'मोर नांव',
'मैं सियाही भाषा सीखत हंव',
'तोर नांव का हे?',
'तुमन कहां ले आय हव?',
'तुमन कइसने होथव?',
'धन्यवाद'],
'Kannada': ['ಹಲೋ.',
'ಹೇ.',
'ಏನು ಅಪ್',
'ನನ್ನ ಹೆಸರು',
'ನಾನು ಸೈನ್ ಭಾಷೆ ಕಲಿಯುತ್ತಿದ್ದೇನೆ',
'ನಿಮ್ಮ ಹೆಸರು ಏನು?',
'ನೀವು ಎಲ್ಲಿಂದ ಬಂದಿದ್ದೀರಿ?',
'ನೀವು ಹೇಗೆ?',
'ಧನ್ಯವಾದಗಳು'],
'Kashmiri (Arabic script)': ['ہیلو ، ہیلو',
'ہیلو',
'کیاہ چُھہ؟',
'مےٚ ناو',
'مَنٛز چھِ سائن لینگُک مطالعہٕ',
'کیاہ چُھ تمہِ ناو؟',
'تمہٕ کیتھہٕ پیٚٹھٕ چھ؟',
'کَتھٕ کَرٕ؟',
'تُہنزِ تشکر'],
'Kashmiri (Devanagari script)': ['हेलो, हेलो',
'हेये',
'क्या छूटा',
'मोर नाव',
'म छु साइन लैंग्वेज सीखे',
'क्या नाम है?',
'तुम कहां से आयी?',
'तुम कइसे छी?',
'शुक्रिया'],
'Magahi': ['हैलो, हैलो',
'हैलो',
'की होलइ?',
'हमर नाम',
'हम साइन लैंग्वेज सीख रहलूं ह',
'तोहर नाम की हइ?',
'तूँ कहाँ से हो?',
'अच्छऽ, अपने कइसन हथिन?',
'धन्यवाद.'],
'Maithili': ['नमस्कार.',
'हाय, हाय, हाय.',
'की भऽ रहल अछि?',
'हमर नाम',
'हम साइन लैंग्वेज सीख रहल छी',
'अहाँक नाम की अछि?',
'अहाँ कतऽ सँ छी?',
'अहाँ की करैत छी?',
'धन्यवाद'],
'Malayalam': ['ഹലോ.',
'ഹായ്.',
'എന്താണാവോ പ്രശ്നം?',
'എന്റെ പേര്',
'ഞാൻ അംബരഭാഷ പഠിക്കുന്നു',
'എന്താ നിന്റെ പേര്?',
'എവിടെ നിന്നാണ് നീ വന്നത്?',
'- എങ്ങിനെയാ നീ?',
'നന്ദി.'],
'Marathi': ['नमस्कार.',
'अरे.',
'काय चाललंय?',
'माझे नाव',
'मी साइन लँग्वेज शिकत आहे',
'तुझं नाव काय?',
'तू कुठून आहेस?',
'तू कशी आहेस?',
'धन्यवाद.'],
'Meitei (Bengali script)': ['হ্যালো',
'ঐহাক্না হায়জরি',
'করি লৈরি',
'ঐগী মমিং',
'ঐহাক্না ময়েক শেংবগী লোন তম্লি',
'অদোমগী মমিং করিনো?',
'অদোম কদায়দগী লাকপা?',
'অদোম্না করম তৌবগে?',
'থাগৎচরি'],
'Burmese': ['ဟိုင်း',
'ဟေး',
'ဘာများများများများများများများများများ',
'ကျွန်မရဲ့နာမည်',
'လက်ရာဘာသာစကား သင်ယူနေ',
'မင်းအမည်က ဘာလဲ',
'ဘယ်ကလာတာလဲ',
'မင်းဘယ်လိုနေလဲ',
'ကျေးဇူးတင်ပါတယ်။'],
'Nepali': ['नमस्कार',
'हेलो',
'के हो',
'मेरो नाम',
'म सानेरी भाषा सिक्दैछु',
'तिम्रो नाम के हो?',
'तिमी कहाँबाट हौ?',
'तिमी कसरी छौ?',
'धन्यवाद'],
'Odia': ['ହାଏ, ହାଏ!',
'ହେଲୋ',
"କ'ଣ ହେଲା?",
'ମୋର ନାମ',
'ମୁଁ ସାଙ୍କେତିକ ଭାଷା ଶିଖୁଛି',
'ତୁମ ନାଁ କଣ?',
'ତୁମେ କେଉଁଠୁ ଆସିଛ?',
'- କେମିତି ଅଛ?',
'ଧନ୍ୟବାଦ'],
'Eastern Panjabi': ['ਹੈਲੋ',
'ਹੈਲੋ',
'ਕੀ ਹੈ',
'ਮੇਰਾ ਨਾਮ',
'ਮੈਂ ਸੈਨਤ ਭਾਸ਼ਾ ਸਿੱਖ ਰਿਹਾ ਹਾਂ',
'ਤੁਹਾਡਾ ਨਾਮ ਕੀ ਹੈ?',
'ਤੁਸੀਂ ਕਿੱਥੋਂ ਆਏ ਹੋ?',
'ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?',
'ਧੰਨਵਾਦ'],
'Sanskrit': ['नमस्कारः',
'हे!',
'किं च',
'मम नाम',
'अहं साइनभाषां सीखिष्यामि',
'भवद्भिः नाम किम्?',
'भवता कस्मान्नि?',
'भवता कीदृशः?',
'धन्यं भव ।'],
'Sinhala': ['හෙලෝ',
'හේයි',
'මොකද වෙන්නේ?',
'මගේ නම',
'මම ලියාපදිංචි භාෂාව ඉගෙන ගන්නවා',
'ඔයාගේ නම මොකක්ද?',
'ඔයා කොහෙන්ද ආවේ?',
'කොහොමද ඔයාට?',
'ස්තුතියි'],
'Sindhi': ['هيلو ، هيلو',
'هيئي',
'ڇا آهي Up',
'منهنجو نالو',
'مون کي اشارو ٻوليءَ جو سکڻ گهرجي',
'تنهنجو نالو ڇا آهي؟',
'تون ڪٿان آيو آهين؟',
'ڪيئن آهين؟',
'شڪر ڪر'],
'Swahili': ['Halo',
'Hey',
'Nini juu',
'Jina Langu',
'Ninajifunza Lugha ya Ishara',
'Jina lako ni nani?',
'Wewe ni kutoka wapi?',
'Wewe unaendeleaje?',
'Asante'],
'Tamil': ['வணக்கம்.',
'ஹேய்',
'என்ன நடக்கிறது',
'என் பெயர்',
'நான் கையொப்ப மொழி கற்கிறேன்',
'உங்கள் பெயர் என்ன?',
'நீ எங்கிருந்து வந்தாய்?',
'எப்படி இருக்கீங்க?',
'நன்றி'],
'Telugu': ['హలో.',
'హే.',
'ఏం అప్ ఉంది',
'నా పేరు',
'నేను సంకేత భాష నేర్చుకుంటున్నాను',
'మీ పేరు ఏమిటి?',
'మీరు ఎక్కడ నుండి?',
'ఎలా మీరు?',
'ధన్యవాదాలు']}


  let temp = 0;
  const Lang = document.querySelector('#language').value;
  for (let i = 0; i < maxPredictions; i++) {
//    if (prediction[i].probability > maximum)  {
//      maximum = prediction[i].probability
    const classPrediction = translation[Lang][i] + ": " + prediction[i].probability.toFixed(2);
    labelContainer.childNodes[i].innerHTML = classPrediction;
      
//    }
  }

  drawPose(pose);
}

function drawPose(pose) {
  if (webcam.canvas) {
    ctx.drawImage(webcam.canvas, 0, 0);
    if (pose) {
      const minPartConfidence = 0.7;
      tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
      tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
    }
  }
}