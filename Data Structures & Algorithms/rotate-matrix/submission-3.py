class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix.reverse()
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]