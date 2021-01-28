from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp[i][j] 表示左上角点到 [i,j] 点的最小路径和

        核心思路跟 62,63题的思路一致，但是需要考虑边界问题，和如何表达计算出的最短路径问题

        针对边界问题，也就是第一行和第一列的最短路径和，等于前一个位置 dp 数组值和当前位置的数字之和，
        为了防止重复计算 dp[0][0] 的值，i, j下标从 1 开始

        定义好 dp 数组后，只需要选择上一个状态 dp 数组中最小的值和当前值相加
        """

        n, m = len(grid), len(grid[0])

        dp = [[0] * m for _ in range(n)]

        # base case
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, m):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
