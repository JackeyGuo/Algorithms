from typing import List


class Solution:
    # 考虑网格中有障碍物
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        定义 dp[i][j] 为到 i,j 格子的总路径
        选择还是两种，向右或者向下，但是这个时候需要考虑格子是否含有障碍物
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # 先判断第一个位置是否为 1
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        else:
            return 0

        for i in range(m):
            for j in range(n):
                # 跳过 [0,0] 位置，因为上面已经处理过特殊情况了
                if i == j == 0: continue

                # 只需要判断 i,j 位置是否为 1
                if obstacleGrid[i][j] == 0:
                    # 判断上一个状态的位置是否为 1，如果是则不能从上一个状态转移过来
                    # 以下不需要判断，因为 [i-1][j] 和 [i][j-1] 会优先遍历，如果有障碍物，会优先置 0
                    # if obstacleGrid[i - 1][j] == 1:
                    #     dp[i - 1][j] = 0
                    # if obstacleGrid[i][j - 1] == 1:
                    #     dp[i][j - 1] = 0
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles(
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]))
