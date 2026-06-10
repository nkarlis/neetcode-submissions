class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box, rowS, colS = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if( board[r][c] in rowS[r] or board[r][c] in colS[c] or
                board[r][c] in box[(r//3, c//3)]):
                    return False
                rowS[r].add(board[r][c])
                colS[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        return True