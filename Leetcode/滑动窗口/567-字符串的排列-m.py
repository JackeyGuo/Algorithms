class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = {}.fromkeys(s1, 0)
        windows = {}.fromkeys(s1, 0)

        for s in s1: needs[s] += 1

        left, right = 0, 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in needs.keys():
                windows[c] += 1
                if windows[c] == needs[c]:
                    valid += 1

            print("扩张", left, right, c, windows, needs, valid)

            # 判断左侧窗口是否要收缩-收缩条件：当右侧与左侧之间的字符数大于或等于 s1 中字符数，开始收缩
            while (right - left) >= len(s1):
                # 判断是否找到了合法的子串
                if valid == len(needs):
                    return True

                d = s2[left]
                left += 1

                if d in needs.keys():
                    if windows[d] == needs[d]:
                        valid -= 1
                    windows[d] -= 1

                print("收缩", left, right, d, windows, needs, valid)

        return False


print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
