from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sw = sorted(nums[i:i + k])

            hk = k // 2
            if k % 2 == 0:
                tmp_res = (sw[hk] + sw[hk - 1]) / 2
            else:
                tmp_res = sw[hk]

            res.append(tmp_res)

        return res


print(Solution().medianSlidingWindow(nums=[1, 4, 2, 3], k=4))
