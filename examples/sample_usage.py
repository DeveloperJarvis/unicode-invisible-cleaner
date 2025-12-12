# # Example usage of the Unicode Invisible Cleaner library
# # old
# from unicode_invisible_cleaner.api import detect_invisible, clean_invisible

# def old_main():
#     # Sample text with invisible Unicode characters
#     sample_text = "Hello, World! \u200B\u200CThis is a test string with invisible characters."

#     # Detect invisible characters
#     detected_items = detect_invisible(sample_text)
#     print("Detected Invisible Characters:", detected_items)
#     # for item in detected_items:
#     #     print(f"Character: {item['character']} at position {item['position']}")

#     # Clean the text by removing invisible characters
#     cleaned_text = clean_invisible(sample_text)
#     print("\nCleaned Text:", cleaned_text)
#     # print(cleaned_text)


#new
from unicode_invisible_cleaner.detector import InvisibleTextDetector
from unicode_invisible_cleaner.cleaner import InvisibleTextRemover
from unicode_invisible_cleaner.normalizer import InputProcessor


def main():
    # Sample text with invisible Unicode characters
    sample_text = "Hello, World! \u200B\u200CThis is a test string with invisible characters."

    # Initialize detector and cleaner
    detector = InvisibleTextDetector()
    cleaner = InvisibleTextRemover()
    normalizer = InputProcessor()

    normalized_text = normalizer.process(sample_text)
    print("Normalized Text:")
    print(normalized_text)
    print()

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