from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        标准滑动窗口解法
        """
        needs = {}.fromkeys(nums, 0)
        windows = {}.fromkeys(nums, 0)
        for num in nums: needs[num] += 1

        max_freq = max(needs.values())

        n = len(nums)
        left, right, res = 0, 0, n

        while right < n:
            c = nums[right]
            right += 1
            windows[c] += 1

            while max(windows.values()) == max_freq:
                # 满足条件，计算子数组长度
                res = min(res, right - left)

                d = nums[left]
                left += 1
                windows[d] -= 1

        return res

    def findShortestSubArray2(self, nums: List[int]) -> int:
        """
        数组遍历法，记录每个数字出现的频次，第一次出现的位置和最后一次出现的位置
        """
        left, right = {}, {}
        counter = collections.Counter()
        # 遍历一次数组，记录每个数字的频次和出现的位置
        for i, num in enumerate(nums):
            # 只记录数字第一次出现的位置
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1

        max_freq = max(counter.values())
        res = len(nums)
        # 对 counter 再次遍历
        for k, v in counter.items():
            if v == max_freq:
                res = min(res, right[k] - left[k] + 1)

        return res


print(Solution().findShortestSubArray2([1, 2, 2, 3, 1, 4, 2]))
