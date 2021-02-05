from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力法：双指针依次遍历判断
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumRevise(self, nums: List[int], target: int) -> List[int]:
        """
        两数之和修改版本，不返回索引，返回元素值
        思路：先排序，然后左右指针相向而行
        """
        n = len(nums)

        nums.sort()

        left, right = 0, n - 1
        while left < right:
            sumAll = nums[left] + nums[right]

            # 根据 sum 和 target 的比较，移动左右指针
            # 元素和大，需要移动右指针，缩小右指针值
            if sumAll > target:
                right -= 1
            # 元素和小，需要移动左指针，增大左指针值
            elif sumAll < target:
                left += 1
            else:
                return [left, right]

    def twoSumRevise2(self, nums: List[int], target: int) -> List[int]:
        """
        两数之和修改版本，不返回索引，返回元素值，并且需要返回多组可能的元素对，但是元素对不能相同
        思路：排序，双指针相向而行，跳过相同元素，去除相同元素对
        通用 N 数和模板
        """
        n = len(nums)

        nums.sort()

        left, right = 0, n - 1
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
                res.extend([low, high])
                while left < right and nums[left] == low: left += 1
                while left < right and nums[right] == high: right -= 1

        return res


print(Solution().twoSumRevise2(nums=[2, 7, 11, 15], target=9))
