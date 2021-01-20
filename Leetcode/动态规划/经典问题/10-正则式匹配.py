class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            if i == 0:
                return False
            # 特别说明：此处需要减一，因为刚开始设定数组的时候加了1
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # 两个空字符串是可以匹配的
        dp[0][0] = True
        # 解决s=""，p="a*"
        for i in range(n + 1):
            for j in range(1, m + 1):
                # 此处也是j-1，因为dp数组+1
                if p[j - 1] != "*":
                    # 判断s[i],p[j]是否相等
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
                else:
                    dp[i][j] |= dp[i][j - 2]
                    # 判断s[i],p[j-1]是否相等
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
        return dp[n][m]


if __name__ == "__main__":
    solution = Solution()
    s = ""
    p = "a*"
    print(solution.isMatch(s, p))
