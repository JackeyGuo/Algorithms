class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        标准滑动窗口框架思路：
        刚开始需要将两个字符的 ASCII 码值的差的绝对值保存为数组，也就是相当于找最长连续子串和小于 maxCost
        """

        n = len(s)

        diffs = []
        for i in range(n):
            diffs.append(abs(ord(s[i]) - ord(t[i])))

        left, right = 0, 0
        cost = 0
        res = 0
        while right < n:
            c = diffs[right]
            right += 1

            cost += c
            # 左指针移动条件：滑窗内的数组和大于最大值
            while cost > maxCost:
                d = diffs[left]
                left += 1

                cost -= d
            # 统计每个滑窗的长度
            res = max(res, right - left)

        return res


print(Solution().equalSubstring(s="abcd", t="abcd", maxCost=0))
