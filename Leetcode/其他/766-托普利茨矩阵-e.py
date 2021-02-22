from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        从第二行第二列开始遍历，依次判断 [i,j] 位置的值是否等于 [i-1,j-1]位置的值
        """
        n, m = len(matrix), len(matrix[0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


print(Solution().isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
