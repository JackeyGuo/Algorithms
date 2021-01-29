class Solution:
    # 方法一：动态规划
    def longestValidParentheses(self, s: str) -> int:
        """
        dp[i] 为以 i 结尾的有效子串长度

        状态转移方程：
        以 '(' 结尾的一定为 0;
        以 ')' 结尾，如果前一个字符 s[i-1] 为 '('，则，通过 dp[i-2] 状态转移过来再 + 2;
                    如果前一个字符为 ')'，需要往前找以 i-1 结尾的有效子串长度 dp[i-1] ，需要判断 i - dp[i-1] - 1 位置的字符串是否为 '('
                    如果是，则从 dp[i - dp[i-1] - 2] 的状态转移过来
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n

        max_length = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

                if dp[i] > max_length:
                    max_length = dp[i]

        return max_length

    # 方法二：栈
    def longestValidParentheses2(self, s: str) -> int:
        """
        对于遇到的每个 ‘(’ ，我们将它的下标放入栈中
        对于遇到的每个 ‘)’ ，我们先弹出栈顶元素表示匹配了当前右括号：
            如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
            如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」

        """


print(Solution().longestValidParentheses(")("))
