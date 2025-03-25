from googletrans import Translator

def chat_with_ai(user_input, target_language):
    translator = Translator()
    translation = translator.translate(user_input, dest=target_language)
    return translation.text

# Example Usage
user_input = input("Enter a sentence to translate: ")
target_language = input("Enter the target language code (e.g., 'fr' for French, 'es' for Spanish'): ")
response = chat_with_ai(user_input, target_language)
print("Translated Sentence:", response)
