import unittest
from unicode_invisible_cleaner.cleaner import InvisibleTextRemover
# from ..src.unicode_invisible_cleaner.cleaner import InvisibleTextRemover

class TestInvisibleTextRemover(unittest.TestCase):

    def setUp(self):
        self.remover = InvisibleTextRemover()

    def test_remove_invisible_characters(self):
        text_with_invisible = "Hello\u200B World\u200C!"
        cleaned_text = self.remover.remove(text_with_invisible)
        self.assertEqual(cleaned_text, "Hello World!")

    def test_no_invisible_characters(self):
        text_without_invisible = "Hello World!"
        cleaned_text = self.remover.remove(text_without_invisible)
        self.assertEqual(cleaned_text, "Hello World!")

    def test_multiple_invisible_characters(self):
        text_with_multiple_invisible = "Hello\u200B World\u200C! \u200DThis is a test."
        cleaned_text = self.remover.remove(text_with_multiple_invisible)
        self.assertEqual(cleaned_text, "Hello World! This is a test.")

    def test_empty_string(self):
        cleaned_text = self.remover.remove("")
        self.assertEqual(cleaned_text, "")

if __name__ == '__main__':
    unittest.main()