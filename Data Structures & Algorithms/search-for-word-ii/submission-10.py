class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)
        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, word, cur):
            if( r not in range(ROWS) or c not in range(COLS) or  (r,c) in visit or
            board[r][c] not in cur.children):
                return 
            visit.add((r, c))
            word += board[r][c]
            cur = cur.children[board[r][c]]
            if cur.isWord:
                res.add(word)
            dfs(r + 1, c, word, cur)
            dfs(r - 1, c, word, cur)
            dfs(r, c + 1, word, cur)
            dfs(r, c - 1, word, cur)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)