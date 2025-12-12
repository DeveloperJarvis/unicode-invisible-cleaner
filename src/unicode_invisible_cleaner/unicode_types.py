class UnicodeCharDef:
    def __init__(self, character: str, code_point: int):
        self.character = character
        self.code_point = code_point

class DetectedItem:
    def __init__(self, char_def: UnicodeCharDef, position: int):
        self.char_def = char_def
        self.position = position

class DetectionReport:
    def __init__(self):
        self.detected_items = []

    def add_item(self, item: DetectedItem):
        self.detected_items.append(item)

    def summary(self):
        return {
            "total_detected": len(self.detected_items),
            "items": [(item.char_def.character, item.position) for item in self.detected_items]
        }