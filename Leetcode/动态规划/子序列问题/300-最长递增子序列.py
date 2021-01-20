from typing import List


class Solution:
    # 300. 最长递增子序列
    """
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
    例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums: return 0

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS(nums))
