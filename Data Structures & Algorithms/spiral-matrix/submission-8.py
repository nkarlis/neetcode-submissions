class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        l, r = 0, len(matrix[0])
        res = []
        while l < r and top < bottom:
            for j in range(l, r):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and top < bottom):
                break
            for j in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][j])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res
            
