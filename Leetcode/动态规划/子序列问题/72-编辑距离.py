from typing import List


class Solution:
    # 72.编辑距离
    """
    二维DP数组，后状态通过前三个状态得到
    """

    def minDistance(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1,
                                   dp[i - 1][j - 1] + 1)
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    str1 = "rad"
    str2 = "apple"
    print(solution.minDistance(str1, str2))
