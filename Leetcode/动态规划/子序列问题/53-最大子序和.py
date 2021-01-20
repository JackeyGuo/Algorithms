from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp 数组的含义: 以 nums[i] 为结尾的「最大子数组和」为 dp[i]。

        dp[i] 有两种「选择」，要么与前面的相邻子数组连接，形成一个和更大的子数组；要么不与前面的子数组连接，自成一派，自己作为一个子数组。
        """
        n = len(nums)
        dp = [0] * n

        # base case 第一个元素前面没有子数组
        dp[0] = nums[0]

        for i in range(1, n):
            # 要么自成一派，要么和前面的子数组合并
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        # 得到 nums 的最大子数组
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
