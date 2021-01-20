from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        @param k:
        @param prices:
        @return:

        for 状态1 in 状态1的所有取值：
            for 状态2 in 状态2的所有取值：
                for ...
                    dp[状态1][状态2][...] = 择优(选择1，选择2...)

        每天都有三种「选择」：买入、卖出、无操作,用 buy, sell, rest 表示这三种选择
        sell 必须在 buy 之后，buy 必须在 sell 之后。那么 rest 操作还应该分两种状态，
        一种是 buy 之后的 rest（持有了股票），一种是 sell 之后的 rest（没有持有股票）。
        还有交易次数 k 的限制，就是说你 buy 还只能在 k > 0 的前提下操作。

        这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，
        第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）
        三维数组表示所以的状态：
        dp[i][k][0 or 1]
        0 <= i <= n-1, 1 <= k <= K
        n 为天数，大 K 为最多交易数
        此问题共 n × K × 2 种状态，全部穷举就能搞定。

        for 0 <= i < n:
            for 1 <= k <= K:
                for s in {0, 1}:
                    dp[i][k][s] = max(buy, sell, rest)

        dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易
        最终答案是 dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润

        """

        """
        状态转移方程：
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              max(   选择 rest  ,             选择 sell      )

        解释：今天我没有持有股票，有两种可能：
        要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
        要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。
        
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                      max(   选择 rest  ,           选择 buy         )
        
        解释：今天我持有着股票，有两种可能：
        要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
        要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。
        
        如果 buy，就要从利润中减去 prices[i]，如果 sell，就要给利润增加 prices[i]
        """
        """
        定义 base case
        dp[-1][k][0] = 0
        解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
        dp[-1][k][1] = -infinity
        解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
        dp[i][0][0] = 0
        解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
        dp[i][0][1] = -infinity
        解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。
        """

        """
        base case：
        dp[-1][k][0] = dp[i][0][0] = 0
        dp[-1][k][1] = dp[i][0][1] = -infinity
        
        状态转移方程：
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        """

        n = len(prices)
        max_k = k
        # 创建三维数组
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        # 以下代码创建三维dp数组，取第三维[0]或[1]时会出错
        # dp = [[[0, 0]] * (max_k + 1) for _ in range(n)]
        # 遇到空数组[]，返回0
        if n == 0: return 0

        # base case
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float("inf")

        # 顺序遍历
        for i in range(n):
            for k in range(1, max_k + 1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))
