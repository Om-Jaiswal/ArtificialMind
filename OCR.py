import easyocr

class OCR:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def changelang(self, lang):
        ## lang accepts a list of languages present in image
        self.reader = easyocr.Reader(lang)

    def recognize(self, img_path, lang=['en']):
        self.changelang(lang)
        txt = self.reader.readtext(img_path, detail = 0)
        clean = ' '.join(txt)
        return clean


def main():
    ocr = OCR()
    print(ocr.recognize('test_mag.jpg', ['mah']))


if __name__ == "__main__":
    main()

    