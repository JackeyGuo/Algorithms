from typing import List


class Solution:
    # k = 2
    def maxProfit(self, K: int, prices: List[int]) -> int:
        """"""
        """
        原始的动态转移方程，没有可化简的地方
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        """
        n = len(prices)
        max_k = K
        # 创建三维数组
        # dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        # 以下方法都可以创建
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(n)]
        # dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]

        # 以下代码创建三维dp数组，取第三维[0]或[1]时会出错
        # dp = [[[0, 0]] * (max_k + 1) for _ in range(n)]
        
        if n == 0: return 0

        # base case
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float("inf")

        # 顺序遍历
        for i in range(n):
            for k in range(1, max_k + 1):
                if i == 0:
                    # 第一天：不持有，收益为0；持有收益为-price[i]
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(2, [2, 4, 1]))
