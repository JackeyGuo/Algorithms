from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                    = max(dp[i-1][1][1], -prices[i])
        解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。

        现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。
        可以进行进一步化简去掉所有 k：
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
        """

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        for i in range(n):
            if i == 0:
                # 第一天：不持有，收益为0；持有收益为-price[i]
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[n - 1][0]

    """
    状态压缩：
    新状态只和相邻的一个状态有关，其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):
    """

    def maxProfitRevise(self, prices: List[int]) -> int:
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -float("inf")

        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfitRevise([7, 1, 5, 3, 6, 4]))
