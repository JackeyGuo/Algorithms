from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        n, m = len(A), len(A[0])

        res = []
        for i in range(n):
            tmp_list = []
            for j in range(m - 1, -1, -1):
                # 用异或取反，也可以用 1-x
                tmp_list.append(A[i][j] ^ 1)

            res.append(tmp_list)
        return res

    def flipAndInvertImage2(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in row[::-1]] for row in A]


print(Solution().flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
