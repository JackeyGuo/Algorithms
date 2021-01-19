from typing import List


class Solution:
    # k = +infinity with cooldown
    def maxProfit(self, prices: List[int]) -> int:
        """"""
        """
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
        """
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float("inf")
        dp_pre_0 = 0  # 代表 dp[i-2][0]
        for i in range(n):
            # 存储之前的值
            temp = dp_i_0
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp

        return dp_i_0

    # 使用原始的动态规划代码，不进行状态转移
    def maxProfitRevise(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        if n == 0:
            return 0

        for i in range(n):
            if i == 0:
                # 第一天：不持有，收益为0；持有，收益为-price[i]
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            elif i == 1:
                # 第二天：不持有，收益根据第一天转移；持有，收益取前一天不持有和前一天持有最大
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], - prices[i])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n - 1][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfitRevise([1, 2, 3, 0, 2]))
