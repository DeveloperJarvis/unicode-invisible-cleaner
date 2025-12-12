import os

INVISIBLE_CHARS = [
            '\u200B',  # Zero Width Space
            '\u200C',  # Zero Width Non-Joiner
            '\u200D',  # Zero Width Joiner
            '\u2060',  # Word Joiner
            '\uFEFF',  # Zero Width No-Break Space
            # Add more invisible characters as needed
        ]

BASE_DIR = os.getcwd() # BASE project directory