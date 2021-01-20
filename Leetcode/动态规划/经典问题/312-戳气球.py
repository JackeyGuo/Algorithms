from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 问题的关键是如何定义dp数组
        # 关键点一：dp[i][j]=x,表示戳破气球 i 和气球 j 之间（开区间，不包括i,j）的所有气球，能获得的最高分数x
        # 关键点二：逆向思维，设定(i, j)中最后被戳破的气球是k，先戳破(i, k)和(k, j)两个区间，最后留下k
        # 关键点三：如何穷举i,j
        n = len(nums)
        points = [1] + nums + [1]

        # 包含0和n+1
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        # 考虑遍历顺序，需要先知道dp[i][k],dp[k][j]，也就是dp数组中第i行和第j列所有元素，所有可以反着遍历
        # i从下到上
        for i in range(n - 1, -1, -1):
            # j从左到右
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])

        return dp[0][n + 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCoins([3, 1, 5, 8]))
