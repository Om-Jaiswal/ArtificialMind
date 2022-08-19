import speech_recognition as sr


class Recognizer:
    def __init__(self, ):
        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()

    def transcribe(self, path, lang='en-IN'):
        # Reading Audio file as source
        # listening the audio file and store in audio_text variable
        with sr.AudioFile(path) as source:
            audio_text = self.r.listen(source)
    
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                text = self.r.recognize_google(audio_text, language = lang)
                print('Converting audio transcripts into text ...')
                print(text)
            
            except:
                print('Sorry.. run again...')


def main():
    recognizer = Recognizer()
    recognizer.transcribe("test_malayalam.wav", lang='ml-IN')


if __name__ == "__main__":
    main()
