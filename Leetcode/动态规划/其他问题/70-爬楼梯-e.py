class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[i] 表示爬到第 i 个台阶需要的方法数
        选择为台阶数，状态为爬一阶或者是二阶
        """
        # 给定 n 是一个正整数，所以不考虑 n=0 的情况，设定为1，则 n 从3开始，需要判断 n=1 和 n=2 的情况
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n + 1)
        # base case
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            # 总的方法数=爬到第 x - 1 级台阶的方案数和爬到第 x - 2 级台阶的方案数的和
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


print(Solution().climbStairs(4))
