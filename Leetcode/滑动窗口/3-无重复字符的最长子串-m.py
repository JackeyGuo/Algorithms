class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = {}.fromkeys(s, 0)

        left, right = 0, 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            # 记录字符 c 的数量
            windows[c] += 1

            print(windows)
            # 当字符 c 的数量大于 1 时，缩小左窗口，保证字符 c 在 windows 中只有一个
            while windows[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                windows[d] -= 1

                print(windows, d, left, right)
            # 收缩窗口完成后更新res
            res = max(res, right - left)

        return res


print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
