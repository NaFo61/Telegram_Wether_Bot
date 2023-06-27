from deep_translator import GoogleTranslator


def get_translate(text):
    Traslator=GoogleTranslator(source='auto', target='ru')
    traslater_text = Traslator.translate(text)
    return traslater_text

