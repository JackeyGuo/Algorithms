class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windows = {}.fromkeys(s, 0)

        left, right = 0, 0
        res = 0
        max_freq = 0  # 当前窗口内出现最多字符的频数
        while right < len(s):
            c = s[right]
            right += 1
            windows[c] += 1

            max_freq = max(max_freq, windows[c])
            # 左侧窗口收缩条件：窗口内除最多的字符数之外的字符数之和大于 k，说明 k 不够用
            # 这里只需要用 if 而不用 while，因为只扩大了一位，如果 left 右移一位不能产生最大子串，右移多次肯定也不能产生
            # 这里窗口内的字符数 = 右指针 - 左指针
            if (right - left) - max_freq > k:
                d = s[left]
                left += 1
                windows[d] -= 1

            res = max(res, right - left)

        return res


print(Solution().characterReplacement(s="ABAB", k=2))
