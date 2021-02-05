from typing import List


class Solution:
    def twoSum(self, nums: List[int], start: int, target: int):
        left, right = start, len(nums) - 1
        res = []

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

        return res

    def threeSum(self, nums: List[int], start, target):

        n = len(nums)

        i = start
        res = []
        # 穷举 threeSum 的第一个数
        while i < n - 1:
            # 对 target - nums[i] 计算 twoSum
            tmp_res = self.twoSum(nums, i + 1, target - nums[i])

            for tpr in tmp_res:
                tpr.insert(0, nums[i])
                res.append(tpr)

            temp_num = nums[i]
            # 跳过第一个数字重复的情况，否则会出现重复结果
            while i < n - 1 and nums[i] == temp_num: i += 1

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        i, res = 0, []
        while i < n - 1:
            # 对 target - nums[i] 计算 twoSum
            tmp_res = self.threeSum(nums, i + 1, target - nums[i])

            for tpr in tmp_res:
                tpr.insert(0, nums[i])
                res.append(tpr)

            temp_num = nums[i]
            # 跳过第一个数字重复的情况，否则会出现重复结果
            while i < n - 1 and nums[i] == temp_num: i += 1

        return res


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
