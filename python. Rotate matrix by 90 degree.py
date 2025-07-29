class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for col in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                mat[top][col], mat[bottom][col] = mat[bottom][col], mat[top][col]
                top += 1
                bottom-=1