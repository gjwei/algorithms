# coding: utf-8
# Author: gjwei
class Trie():
    def __init__(self):
        self.root = {}

    def add(self, word):
        tree = self.root
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]

        tree['word'] = True

    def search(self, word):
        root = self.root
        for char in word:
            if char in root:
                root = root[char]
            else:
                return False
        return 'word' in root and root['word']

    def delete(self, word):
        # 貌似无法删除哎，因为不知道其他的word是不是和这个word有重合的地方。
        pass