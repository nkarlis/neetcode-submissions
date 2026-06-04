class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowS, colS, boxS = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowS[r] or board[r][c] in colS[c] or
                board[r][c] in boxS[(r//3,c//3)]):
                    return False
                rowS[r].add(board[r][c])
                colS[c].add(board[r][c])
                boxS[(r//3,c//3)].add(board[r][c])
        return True