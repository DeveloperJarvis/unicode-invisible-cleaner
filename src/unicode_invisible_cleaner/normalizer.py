class InputProcessor:
    # def __init__(self, text):
    #     self.text = text

    # def normalize(self):
    #     self.text = self._remove_unwanted_characters(self.text)
    #     self.text = self._ensure_consistent_encoding(self.text)
    #     return self.text

    # def _remove_unwanted_characters(self, text):
    #     # Implement logic to remove unwanted characters
    #     return text

    # def _ensure_consistent_encoding(self, text):
    #     # Implement logic to ensure consistent encoding
    #     return text

    def __init__(self):
        pass

    def normalize(self, text: str) -> str:
        """Minimal behaviour expected by tests."""
        return text.strip()
    
    def process(self, text: str) -> str:
        """Alias for normalize(), required by tests."""
        return self.normalize(text)
