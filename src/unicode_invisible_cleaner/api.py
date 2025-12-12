from .detector import InvisibleTextDetector
from .cleaner import InvisibleTextRemover

def detect_invisible(text):
    # Implement detection logic for invisible Unicode characters
    detector = InvisibleTextDetector()
    return detector.detect(text)

def clean_invisible(text):
    # Implement cleaning logic to remove invisible Unicode characters
    remover = InvisibleTextRemover()
    return remover.clean(text)

def detect_and_clean(text):
    detected = detect_invisible(text)
    cleaned = clean_invisible(text)
    return detected, cleaned