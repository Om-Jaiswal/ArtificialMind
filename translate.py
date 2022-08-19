from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Translate:
    def __init__(self, tok_path="./model/tokenizer-nllb-600M", mod_path="./model/seq2seqLM-nllb-600M"):
        self.tokenizer = AutoTokenizer.from_pretrained(tok_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(mod_path)
    
    def translate(self, text, lang="hin_Deva"):
        # article = "Hello"
        inputs = self.tokenizer(text, return_tensors="pt")
        translated_tokens = self.model.generate(
            **inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id[lang], max_length=30
        )
        translation = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

        return translation


if __name__ == "__main__":
    translator = Translate()
    print(translator.translate(text="How are you doing?"))