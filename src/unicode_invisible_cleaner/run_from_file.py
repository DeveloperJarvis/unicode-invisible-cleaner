# file: run_from_file.py
from config import BASE_DIR
from unicode_invisible_cleaner.api import detect_invisible, clean_invisible


def run_from_file(input_file):
    # Read text from input file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Detect invisible characters
    detected_characters = detect_invisible(text)
    print("Detected Invisible Characters:")
    print(detected_characters)

    # clean the text
    cleaned = clean_invisible(text)
    print("\nCleaned Text:")
    print(cleaned)
