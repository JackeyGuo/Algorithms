from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i] 表示凑成总金额 i 所需的最少硬币个数

        状态：总金额，选择：能凑出 or 不能凑出

        """
        if amount == 0: return 0

        # 初始化 dp 数组为为正无穷，便于后续取最小值
        dp = [float("inf")] * (amount + 1)
        # base case
        dp[0] = 0

        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(1, amount + 1):
            # 内层 for 循环在求所有选择的最小值
            for c in coins:
                # 目标金额小于硬币，无解
                if i < c: continue
                # 选择最小值
                dp[i] = min(dp[i],  # 不能凑出，选择自身的最少硬币数
                            dp[i - c] + 1)  # 能凑出，从 i - c 的状态转移过来

        return -1 if dp[amount] == float("inf") else dp[amount]


print(Solution().coinChange(coins=[1], amount=1))
