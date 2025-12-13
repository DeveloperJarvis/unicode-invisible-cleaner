import unittest
from unicode_invisible_cleaner.detector import InvisibleTextDetector

class TestInvisibleTextDetector(unittest.TestCase):

    def setUp(self):
        self.detector = InvisibleTextDetector()

    def test_detect_invisible_characters(self):
        text_with_invisible = "Hello\u200BWorld"  # Contains zero-width space
        detected = self.detector.detect(text_with_invisible)
        self.assertIn('\u200B', detected)

    def test_no_invisible_characters(self):
        text_without_invisible = "Hello World"
        detected = self.detector.detect(text_without_invisible)
        self.assertEqual(detected, [])

    def test_multiple_invisible_characters(self):
        text_with_multiple = "Hello\u200BWorld\u200C!"
        detected = self.detector.detect(text_with_multiple)
        self.assertIn('\u200B', detected)
        self.assertIn('\u200C', detected)

    def test_empty_string(self):
        detected = self.detector.detect("")
        self.assertEqual(detected, [])

if __name__ == '__main__':
    unittest.main()
