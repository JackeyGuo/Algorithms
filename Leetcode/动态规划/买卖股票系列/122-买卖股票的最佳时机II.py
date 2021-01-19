from typing import List


class Solution:
    # k = +infinity
    def maxProfit(self, prices: List[int]) -> int:
        """"""
        """
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                    = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
        
        我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        """

        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float("inf")

        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])

        return dp_i_0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
