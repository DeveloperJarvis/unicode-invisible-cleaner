# regex_map.py

import re

# Regex patterns for detecting invisible Unicode characters
INVISIBLE_CHARACTERS_REGEX = re.compile(
    r'[\u200B-\u200F\u202A-\u202E\u2060\uFEFF]'
)

def find_invisible_characters(text):
    """
    Returns a list of invisible characters found in the given text.
    """
    return INVISIBLE_CHARACTERS_REGEX.findall(text)

def remove_invisible_characters(text):
    """
    Removes invisible characters from the given text.
    """
    return INVISIBLE_CHARACTERS_REGEX.sub('', text)
