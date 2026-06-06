class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        # 3 4
        # 1 2

        #3 1
        #4 2
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]