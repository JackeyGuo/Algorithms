from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs = {}.fromkeys(p, 0)
        windows = {}.fromkeys(p, 0)

        for c in p: needs[c] += 1

        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1

            if c in needs.keys():
                windows[c] += 1
                if windows[c] == needs[c]:
                    valid += 1

            while (right - left) >= len(p):

                if valid == len(needs):
                    res.append(left)

                d = s[left]
                left += 1

                if d in needs.keys():
                    if windows[d] == needs[d]:
                        valid -= 1
                    windows[d] -= 1

        return res


print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
