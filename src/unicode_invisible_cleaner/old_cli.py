# CLI for Invisible Unicode Cleaner

import argparse
from unicode_invisible_cleaner.api import detect_invisible, clean_invisible

def main():
    parser = argparse.ArgumentParser(description="Invisible Unicode Cleaner")
    parser.add_argument("text", type=str, help="Text to process")
    parser.add_argument("--clean", action="store_true", help="Remove invisible characters from the text")
    parser.add_argument("--detect", action="store_true", help="Detect invisible characters in the text")
    
    args = parser.parse_args()

    if args.detect:
        detected = detect_invisible(args.text)
        print("Detected invisible characters:", detected)
    
    if args.clean:
        cleaned_text = clean_invisible(args.text)
        print("Cleaned text:", cleaned_text)

if __name__ == "__main__":
    main()
