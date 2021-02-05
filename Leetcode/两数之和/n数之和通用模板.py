from typing import List


class Solution:
    # 调用这个函数之前一定要先给 nums 排序
    def nSumTarget(self, nums, n, start, target):

        size = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or size < n: return res

        # 2Sum 是 base case
        if n == 2:
            # 双指针操作
            left, right = start, len(nums) - 1
            while left < right:
                low, high = nums[left], nums[right]
                sumAll = low + high

                # 元素和大，需要移动右指针，缩小右指针值
                if sumAll > target:
                    while left < right and nums[right] == high: right -= 1
                # 元素和小，需要移动左指针，增大左指针值
                elif sumAll < target:
                    while left < right and nums[left] == low: left += 1
                else:
                    res.append([low, high])
                    while left < right and nums[left] == low: left += 1
                    while left < right and nums[right] == high: right -= 1
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            for i in range(start, size):
                tmp_res = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])

                for tpr in tmp_res:
                    tpr.insert(0, nums[i])
                    res.append(tpr)
                while i < size - 1 and nums[i] == nums[i + 1]: i += 1

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # n 为 4，从 nums[0] 开始计算和为 target 的四元组
        return self.nSumTarget(nums, 4, 0, target)


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
