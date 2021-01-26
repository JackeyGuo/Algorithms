class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        题目描述：给你一个字符串 s，找到 s 中最长的回文子串。
        dp[i][j] 表示 i...j 是否为回文子串

        回文串的定义展开讨论：
        如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
        如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
        如果里面的子串是回文，整体就是回文串；
        如果里面的子串不是回文串，整体就不是回文串
        """
        n = len(s)
        # 特殊情况 s 小于2
        if n < 2: return s

        dp = [[False] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = True

        # 定义最大长度和初始指针
        max_len = 1
        start = 0
        # 遍历顺序为沿着Y轴竖着遍历，先遍历 Y 在遍历 X 或者 斜着遍历
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # 相等的情况下，判断 dp[i+1][j-1] 是否为回文串，但是需要注意边界，j-1-(i+1)>=1，相当于 j - i >=3
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]


print(Solution().longestPalindrome("babad"))
