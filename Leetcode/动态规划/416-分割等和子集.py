from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 分割等和数组，可以转换为0-1背包问题，背包容量为sum(数组和)/2，只要能装入背包，剩下的数字和一定也等于sum(数组和)/2
        # dp[i][j]=x，表示对于前 i 个物品，当前背包的容量为 j 时，
        # 若 x 为 true，则说明可以恰好将背包装满，若 x 为 false，则说明不能恰好将背包装满。
        n = len(nums)
        # 和为奇数时，不可能划分成两个和相等的集合
        if sum(nums) % 2 != 0: return False
        sum_half = sum(nums) // 2

        dp = [[False] * (sum_half + 1) for _ in range(n + 1)]
        # base case 空数组为True
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, sum_half + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][sum_half]

    # 状态压缩后代码，一般压缩i
    # dp[j] 其实就相当于 dp[i-1][j]
    def canPartition_new(self, nums: List[int]) -> bool:
        n = len(nums)
        # 和为奇数时，不可能划分成两个和相等的集合
        if sum(nums) % 2 != 0: return False
        sum_half = sum(nums) // 2

        dp = [False] * (sum_half + 1)
        # base case
        dp[0] = True
        for i in range(1, n + 1):
            # j 应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，以免之前的结果影响其他的结果。
            for j in range(sum_half, -1, -1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]

        return dp[sum_half]


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition_new([1, 5, 11, 5]))
