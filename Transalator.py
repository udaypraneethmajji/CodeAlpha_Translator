from deep_translator import GoogleTranslator

print("=== Language Translator ===")

text = input("Enter text: ")
target_lang = input("Enter target language (hi=Hindi, fr=French, es=Spanish): ")

try:
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    print("Translated Text:", translated)
except:
    print("Error: Invalid language code or internet issue")