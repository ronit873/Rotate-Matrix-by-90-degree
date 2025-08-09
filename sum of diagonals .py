from typing import List
class Solution:
    def sumDiagonal(self, N : int , M : List[List[int]] ) -> int :
        # code here
        sum = 0
        for i in range(N):
            sum += M[i][i]
        return sum