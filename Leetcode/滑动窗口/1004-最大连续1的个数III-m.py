from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        windows = {}.fromkeys(A, 0)
        n = len(A)

        left, right = 0, 0
        res = 0
        while right < n:
            c = A[right]
            right += 1
            windows[c] += 1

            while windows[0] > K:
                d = A[left]
                left += 1
                windows[d] -= 1

            res = max(res, right - left)

        return res


print(Solution().longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))
