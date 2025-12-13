"""
This package provides functionality for detecting and removing invisible Unicode text characters.
"""

from .detector import InvisibleTextDetector
from .cleaner import InvisibleTextRemover
from .normalizer import InputProcessor
from .api import detect_invisible, clean_invisible, detect_and_clean
# from .utils import some_utility_function  # Example utility function import
from .utils import remove_invisible_unicode, is_invisible_unicode, detect_invisible_unicode
from .unicode_types import UnicodeCharDef, DetectedItem, DetectionReport  # Example type imports

__all__ = [
    "InvisibleTextDetector",
    "InvisibleTextRemover",
    "InputProcessor",
    "detect_invisible",
    "clean_invisible",
    "detect_and_clean",
    "remove_invisible_unicode",
    "is_invisible_unicode",
    "detect_invisible_unicode",
    "UnicodeCharDef",
    "DetectedItem",
    "DetectionReport",
]
