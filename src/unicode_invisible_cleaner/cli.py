# CLI for Invisible Unicode Cleaner

import argparse
from unicode_invisible_cleaner.detector import InvisibleTextDetector
from unicode_invisible_cleaner.cleaner import InvisibleTextRemover
from unicode_invisible_cleaner.normalizer import InputProcessor

def main():
    parser = argparse.ArgumentParser(
        description="Invisible Unicode Cleaner"
    )
    parser.add_argument("text", type=str, help="Text to process")
    parser.add_argument(
        "--clean", action="store_true", help="Remove invisible characters for the text"
    )
    parser.add_argument(
        "--detect", action="store_true", help="Detect invisible characters in the text"
    )

    args = parser.parse_args()

    detector = InvisibleTextDetector()
    cleaner = InvisibleTextRemover()
    normalizer = InputProcessor()

    # Normaliza input
    normalized_text = normalizer.process(args.text)

    if args.detect:
        # Detect invisible characters with positions
        dectected_items = [(i, char) for i, char in 
                        enumerate(normalized_text) if char in
                        detector.invisible_characters]
        print("Detected Invisible Characters:")
        for pos, char in dectected_items:
            print(f"Character: {repr(char)} at position {pos}")
        print(f"Total detected: {len(dectected_items)}\n")

        # Clean text
        cleaned_text = cleaner.clean(normalized_text)
        print("Cleaned Text:")
        print(cleaned_text)

if __name__ == "__main__":
    main()
