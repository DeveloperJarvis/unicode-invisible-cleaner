class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_character = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, character):
        node = self.root
        for char in character:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_character = True

    def search(self, character):
        node = self.root
        for char in character:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_character

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, character):
        def _delete(node, char, depth):
            if not node:
                return None

            if depth == len(char):
                if node.is_end_of_character:
                    node.is_end_of_character = False
                if not node.children:
                    return None
                return node

            char_index = char[depth]
            node.children[char_index] = _delete(node.children.get(char_index), char, depth + 1)

            if not node.children and not node.is_end_of_character:
                return None
            return node

        _delete(self.root, character, 0)