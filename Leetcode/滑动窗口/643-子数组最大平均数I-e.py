from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        暴力法超出时间限制
        """
        # n = len(nums)
        #
        # max_ave = -float("inf")
        # for i in range(n - k + 1):
        #     max_ave = max(max_ave, sum(nums[i:i + k]) / k)
        # return max_ave

        """
        滑动窗口法：
        首先先对 nums[:k] 前 k 个数求和，得到第一组最大和；
        然后依次滑动右指针，直到 nums 数组末尾；
        左指针移动条件：右指针 - 左指针的长度大于 k 时，移动左指针，也就是控制 right - left == k
        """
        n = len(nums)
        left, right = 0, k
        sumAll = sum(nums[:k])
        max_res = [sumAll]
        while right < n:
            c = nums[right]
            right += 1
            sumAll += c

            if right - left > k:
                d = nums[left]
                left += 1
                sumAll -= d

            if right - left == k:
                max_res.append(sumAll)

        return max(max_res) / k


print(Solution().findMaxAverage([5], 1))
