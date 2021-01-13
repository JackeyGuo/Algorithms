class Solution:
    # 651.四键键盘
    def maxA(self, N: int) -> int:
        # dp[i] 表示 i 次操作后最多能显示多少个 A
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            # 第 i 次选择按 A 键
            dp[i] = dp[i - 1] + 1
            for j in range(2, i + 1):
                # 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
                # 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                # 状态二选一：选择按 A 键还是按 C-V
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        #  N 次按键之后最多有几个 A
        return dp[N]


if __name__ == "__main__":
    solution = Solution()
    number = 7
    print(solution.maxA(number))
