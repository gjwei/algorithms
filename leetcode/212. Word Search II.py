# coding: utf-8

class Trie():
    def __init__(self):
        self.root = {}

    def add(self, word):
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['word'] = True

    def delete(self, word):
        root = self.root
        for c in word:
            root = root[c]
        root.pop('word')
        return


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # build Trie
        trie = Trie()
        for word in words:
            trie.add(word)
        result = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie.root:
                    w = self.backtracking(board, i, j, trie.root, [])
                    if w is None:
                        continue
                    result.append(w)
                    trie.delete(w)
        return result
                    
        
    def backtracking(self, board, row, col, root, word_list):
        
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[row])) or board[row][col] not in root or board[row][col] == '#':
            return None
        if 'word' in root:
            return ''.join(word_list)
        c = board[row][col]
        word_list.append(board[row][col])
        root = root[board[row][col]]
        board[row][col] = '#'

        result = self.backtracking(board, row - 1, col, root, word_list) or \
                 self.backtracking(board, row + 1, col, root, word_list) or \
                 self.backtracking(board, row, col - 1, root, word_list) or \
                 self.backtracking(board, row, col + 1, root, word_list)
        board[row][col] = c

        return result
        