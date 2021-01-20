from typing import List


class Solution:
    # 674. 最长连续递增序列
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        依次循环遍历，判断i+1位置是否大于i位置元素，满足条件count+1，
            不满足条件，判断临时count是否最大，然后count+1
        """
        if len(nums) == 0:
            return 0
        count = maxcount = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        return max(maxcount, count)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 4, 7]
    print(solution.findLengthOfLCIS(nums))
