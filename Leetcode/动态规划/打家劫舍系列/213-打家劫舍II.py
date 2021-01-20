from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        首尾房间不能同时被抢，那么只可能有三种不同情况: 要么都不被抢；要么第一间房子被抢最后一间不抢；要么最后一间房子被抢第一间不抢
        只要比较情况二和情况三就行了，因为这两种情况对于房子的选择余地比情况一大，房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小。
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        return max(self.robRange(nums, 0, n - 1),
                   self.robRange(nums, 1, n))

    def robRange(self, nums, start, end):
        n = end - start
        nums = nums[start:end + 1]

        dp = [0] * n
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1, 2, 1, 1]))
