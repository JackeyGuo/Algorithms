from typing import List


class Solution:
    # k = +infinity with fee
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        每次交易要支付手续费，只要把手续费从利润中减去即可。改写方程：
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        解释：相当于买入股票的价格升高了。
        在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
        """
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float("inf")

        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])

        return dp_i_0

    # 使用原始的动态规划代码，不进行状态转移
    def maxProfitRevise(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        if n == 0: return 0

        for i in range(n):
            if i == 0:
                # 第一天：不持有，收益为0；持有，收益为-price[i]
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfitRevise([1, 3, 2, 8, 4, 9], 2))
