import unittest
from unicode_invisible_cleaner.detector import InvisibleTextDetector
from unicode_invisible_cleaner.cleaner import InvisibleTextRemover
from unicode_invisible_cleaner.normalizer import InputProcessor

class TestInvisibleTextIntegration(unittest.TestCase):

    def setUp(self):
        self.detector = InvisibleTextDetector()
        self.cleaner = InvisibleTextRemover()
        self.normalizer = InputProcessor()

    def test_integration_detection_and_removal(self):
        input_text = "Hello\u200B World\u200C!"  # Contains invisible characters
        normalized_text = self.normalizer.process(input_text)
        detected_items = self.detector.detect(normalized_text)
        cleaned_text = self.cleaner.remove(normalized_text)

        self.assertGreater(len(detected_items), 0, "Should detect invisible characters")
        self.assertNotIn("\u200B", cleaned_text, "Cleaned text should not contain zero-width space")
        self.assertNotIn("\u200C", cleaned_text, "Cleaned text should not contain zero-width non-joiner")

    def test_integration_empty_input(self):
        input_text = ""
        normalized_text = self.normalizer.process(input_text)
        detected_items = self.detector.detect(normalized_text)
        cleaned_text = self.cleaner.remove(normalized_text)

        self.assertEqual(len(detected_items), 0, "Should not detect invisible characters in empty input")
        self.assertEqual(cleaned_text, "", "Cleaned text should be empty for empty input")

if __name__ == '__main__':
    unittest.main()
