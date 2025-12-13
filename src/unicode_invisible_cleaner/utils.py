from config import INVISIBLE_CHARS

def remove_invisible_unicode(text):
    invisible_chars = INVISIBLE_CHARS
    for char in invisible_chars:
        text = text.replace(char, '')
    return text

def is_invisible_unicode(char):
    return char in INVISIBLE_CHARS

def detect_invisible_unicode(text):
    return [char for char in text if is_invisible_unicode(char)]
