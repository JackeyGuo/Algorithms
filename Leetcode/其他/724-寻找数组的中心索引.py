from typing import List


class Solution:
    # 暴力法，循环 i, 依次判断 i 的左右两侧和是否一致
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

    # 一次循环即可判断，满足条件：a + x + a = s，即可满足 i 左右两侧相等
    def pivotIndex2(self, nums: List[int]) -> int:
        n = len(nums)
        sumAll = sum(nums)
        sumHalf = 0

        for i in range(n):
            # 满足条件返回 i 的位置，反之继续累计 a 的值，最坏情况循环 n 次
            if sumHalf * 2 + nums[i] == sumAll:
                return i

            sumHalf += nums[i]

        return -1


print(Solution().pivotIndex2([1, 2, 3]))
