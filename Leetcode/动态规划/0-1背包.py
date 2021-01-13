class Solution:
    def knapsack(self, N, W, wt, val):

        # dp[n][w] 表示前i个物品，背包的容量为w，能装下的最大价值
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        # base case dp[0][...]=0, dp[...][0]=0
        for n in range(1, N + 1):
            for w in range(1, W + 1):
                # 判断当前加上当前物品，是否超出背包容量
                if w - wt[n - 1] < 0:
                    # 背包容量不够，选择不装入背包
                    dp[n][w] = dp[n - 1][w]
                else:
                    dp[n][w] = max(dp[n - 1][w],  # 不装
                                   dp[n - 1][w - wt[n - 1]] + val[n - 1])  # 装入背包

        return dp[N][W]


if __name__ == "__main__":
    N, W = 3, 4
    wt = [2, 1, 3]  # 第i个物品的重量
    val = [4, 2, 3]  # 第i个物品的价值

    solution = Solution()
    print(solution.knapsack(N, W, wt, val))
