from config import INVISIBLE_CHARS

class InvisibleTextDetector:
    def __init__(self):
        self.invisible_characters = self.load_invisible_characters()

    def load_invisible_characters(self):
        # Load a set of invisible Unicode characters
        return INVISIBLE_CHARS

    def detect(self, text, with_positions=False):
        """Return only invisible characters, not (index, char)."""
        if with_positions:
                detected = []
                for index, char in enumerate(text):
                    if char in self.invisible_characters:
                        detected.append((index, char))
                return detected
        return [char for char in text if char in self.invisible_characters]

    def report(self, text):
        detected_items = self.detect(text)
        return {
            'text': text,
            'detected': detected_items,
            'count': len(detected_items)
        }