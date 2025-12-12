from config import INVISIBLE_CHARS

class InvisibleTextRemover:
    INVISIBLE_CHARS = INVISIBLE_CHARS

    def __init__(self, rules=None):
        self.rules = rules if rules is not None else []

    def remove_invisible_characters(self, text):
        if self.rules:
            for rule in self.rules:
                text = rule.apply(text)
        for ch in self.INVISIBLE_CHARS:
            text = text.replace(ch, '')
        return text

    def clean(self, text):
        """Public API exptected by api.py"""
        return self.remove_invisible_characters(text)
    
    def add_rule(self, rule):
        self.rules.append(rule)

    def clear_rules(self):
        self.rules.clear()
    
    def remove(self, text):
        """Public method expected by tests."""
        return self.remove_invisible_characters(text)