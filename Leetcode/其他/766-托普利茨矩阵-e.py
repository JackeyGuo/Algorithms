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

    # 扩展版本，只循环一次
    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        """
        从第一行开始遍历，依次判断 [i:j] 位置的值是否等于 [i+1:j]位置的值
        也就是利用 Python 自带的切片，判断第一行前 n 个数字是否与下一行的后 n 个数字是否一致
        """
        n, m = len(matrix), len(matrix[0])

        for i in range(n - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True


print(Solution().isToeplitzMatrix2(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
