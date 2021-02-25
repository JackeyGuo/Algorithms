from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        依次遍历原始矩阵，对新矩阵重新赋值
        """
        n, m = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                res[j][i] = matrix[i][j]

        return res


print(Solution().transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
