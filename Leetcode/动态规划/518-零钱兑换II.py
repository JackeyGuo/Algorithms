from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 状态有两个，就是「背包的容量」和「可选择的物品」，选择就是「装进背包」或者「不装进背包」嘛，背包问题的套路都是这样。
        # 若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法。

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # base case, 不使用任何硬币面值，就无法凑出任何金额；如果凑出的目标金额为 0，那么“无为而治”就是唯一的一种凑法。
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # 由于物品无限，所以 dp[i][...] 不需要i-1,想求的 dp[i][j] 是「共有多少种凑法」，所以 dp[i][j] 的值应该是以上两种选择的结果之和：
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]  # 不使用 coins[i] 这个面值的硬币，那么凑出面额 j 的方法数 dp[i][j] 应该等于 dp[i-1][j]，继承之前的结果。
        return dp[n][amount]


if __name__ == "__main__":
    solution = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(solution.change(amount, coins))
