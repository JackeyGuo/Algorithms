from typing import List


class Solution:
    def longestPalindromeSubseq(self, str1):
        n = len(str1)

        # 反着遍历，只遍历右上半部分, y的第一个位置比x大1，最终位置为n
        """
        (3, 4)
        (2, 3),(2, 4)
        (1, 2),(...),(1, 4)
        (0, 1),(...),(0, 4)
        """
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 状态转移方程
                if str1[i] == str1[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1],
                                   dp[i + 1][j])
        # 整个 s 的最长回文子串长度
        return dp[0][n - 1]

    def longestPalindromeSubseq_new(self, str1):
        # 状态压缩代码
        # dp[j]代替dp[i+1][j], dp[j-1]代替dp[i][j-1], 需要存储dp[i+1][j-1]
        n = len(str1)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            # 存储dp[i+1][j-1]
            pre = 0
            for j in range(i + 1, n):
                # 覆盖之前先存值
                temp = dp[j]
                if str1[i] == str1[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[n - 1]


if __name__ == "__main__":
    solution = Solution()
    str1 = "abxab"
    print(solution.longestPalindromeSubseq(str1))
