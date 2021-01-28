class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        定义 dp[i][j] 为到 i,j 格子的总路径
        两种选择，向下或者向右，总路径为两个选择之和

        第二种解法：排列组合

        需要往下走 n-1 步，往右走 m-1 步，总共需要走 n+m-2 步。
        无论往右走还是往下走他的总的步数是不会变的。也就相当于总共要走 n+m-2 步，往右走 m-1 步总共有多少种走法，
        很明显这就是一个排列组合问题，公式如下

        """

        dp = [[0] * n for _ in range(m)]

        # base case，第 1 行和第 1 列都为 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 横竖遍历都可以
        for i in range(1, m):
            for j in range(1, n):
                # 只有两种选择
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePaths_2(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


print(Solution().uniquePaths(m=3, n=3))
