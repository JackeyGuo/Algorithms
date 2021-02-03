class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = {}.fromkeys(t, 0)
        windows = {}.fromkeys(t, 0)

        for c in t: needs[c] += 1

        left, right = 0, 0
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start, length = 0, len(s) + 1
        while right < len(s):
            c = s[right]
            right += 1

            # 判断 c 字符是否在 needs 字典的 key 中
            if c in needs.keys():
                # c 字符在 needs 中，windows 中字符数 +1
                windows[c] += 1
                # 判断 windows 中的字符是否已全部包含 needs 中的字符，只需要满足找到 needs 中的字符就行，valid +1
                if windows[c] == needs[c]:
                    valid += 1

            # print(left, right, c, windows, needs, valid)

            # 当 windows 中的字符已全部包含 needs 中的字符，准备收缩左侧窗口
            while valid == len(needs):
                # 在这里更新最小覆盖子串
                if (right - left) < length:
                    start = left
                    length = right - left

                # d 是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 进行窗口内数据的一系列更新
                # 首先判断 d 是否在 needs 中
                if d in needs.keys():
                    # 判断去掉 d 字符后，windows 和 needs 中的值是否一致，一致后，valid-1
                    if windows[d] == needs[d]:
                        valid -= 1
                    # 去掉了 windows 中的 d 字符
                    windows[d] -= 1

                # print(left, right, d, windows, needs, valid, lengh)

        return s[start: start + length] if length != len(s) + 1 else ""


# ADOBECODEBANC
print(Solution().minWindow(s="EBBANCF", t="ABC"))
