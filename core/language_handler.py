from googletrans import Translator
import re

translator = Translator()

def detect_and_translate(text):
    """Detect language and translate to English for processing"""
    try:
        detection = translator.detect(text)
        if detection.lang != 'en':
            translated = translator.translate(text, dest='en')
            return translated.text, detection.lang
        return text, 'en'
    except:
        return text, 'en'

def translate_response(text, target_lang):
    """Translate response back to user's language"""
    if target_lang == 'en':
        return text
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except:
        return text

# Common agricultural terms in local languages
SWAHILI_TERMS = {
    'pest': 'mdudu',
    'plant': 'panda',
    'harvest': 'vuna',
    'rain': 'mvua',
    'maize': 'mahindi'
}

KIKUYU_TERMS = {
    'pest': 'kihururu',
    'plant': 'haanda',
    'harvest': 'getha',
    'rain': 'mbura'
}