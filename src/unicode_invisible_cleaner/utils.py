def remove_invisible_unicode(text):
    invisible_chars = [
        '\u200B',  # Zero Width Space
        '\u200C',  # Zero Width Non-Joiner
        '\u200D',  # Zero Width Joiner
        '\u2060',  # Word Joiner
        '\uFEFF',  # Zero Width No-Break Space
    ]
    for char in invisible_chars:
        text = text.replace(char, '')
    return text

def is_invisible_unicode(char):
    return char in [
        '\u200B',  # Zero Width Space
        '\u200C',  # Zero Width Non-Joiner
        '\u200D',  # Zero Width Joiner
        '\u2060',  # Word Joiner
        '\uFEFF',  # Zero Width No-Break Space
    ]

def detect_invisible_unicode(text):
    return [char for char in text if is_invisible_unicode(char)]