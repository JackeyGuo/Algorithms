from typing import List

"""
回溯算法框架：
def backtrace(路径，选择列表):
    if 满足结束条件：
        result.add(路径)
    
    for 选择 in 选择列表：
        做选择
        backtrace(路径，选择列表)
        撤销选择
"""


class Solution:

    # def __init__(self):
    #     self.result = 0
    #
    # # 回溯算法模板
    # def backtrace(self, nums, i, rest):
    #     # base case
    #     if i == len(nums):
    #         if rest == 0: self.result += 1
    #         return
    #
    #     # 给 nums[i] 选择 - 号,相当于把 target 减到 0
    #     rest += nums[i]
    #     # 穷举 nums[i + 1]
    #     self.backtrace(nums, i + 1, rest)
    #     # 撤销选择
    #     rest -= nums[i]
    #
    #     # 给 nums[i] 选择 + 号
    #     rest -= nums[i]
    #     # 穷举 nums[i + 1]
    #     self.backtrace(nums, i + 1, rest)
    #     # 撤销选择
    #     rest += nums[i]
    #
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     """
    #     回溯法：两种选择，给一个正号 + 或者一个负号 -
    #
    #     伪代码：
    #     def backtrace(nums, i):
    #         if i == len(nums):
    #             if 达到 target:
    #                 result += 1
    #
    #         for op in {+1, -1}:
    #             选择 op * nums[i]
    #             # 穷举 nums[i + 1] 的选择
    #             backtrace(nums, i+1)
    #             撤销选择
    #     """
    #     if len(nums) == 0: return 0
    #     self.backtrace(nums, 0, S)
    #     return self.result

    def findTargetSumWaysRevise(self, nums: List[int], S: int) -> int:
        """
        把 nums 划分成两个子集 A 和 B，分别代表分配 + 的数和分配 - 的数，那么他们和 target 存在如下关系：
        sum(A) - sum(B) = target
        sum(A) = target + sum(B)
        sum(A) + sum(A) = target + sum(B) + sum(A)
        2 * sum(A) = target + sum(nums)

        可以推出：sum(A) = (target + sum(nums)) / 2
        把原问题转化成：nums 中存在几个子集 A，使得 A 中元素的和为 (target + sum(nums)) / 2

        dp[i][j] = x 表示，若只在前 i 个物品中选择，若当前背包的容量为 j，则最多有 x 种方法可以恰好装满背包
        """
        sumAll = sum(nums)

        # 这两种情况，不可能存在合法的子集划分
        if (sumAll < S) or ((S + sumAll) % 2 == 1): return 0

        sums = (S + sumAll) // 2
        # 计算 nums 中有几个子集的和为 sums
        n = len(nums)
        dp = [[0] * (sums + 1) for _ in range(n + 1)]
        # base case 空数组为True
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            # 注意子集 j 的容量可以为0
            for j in range(0, sums + 1):
                if j < nums[i - 1]:
                    # 背包的空间不足，只能选择不装物品 i
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 两种选择的结果之和
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

        return dp[n][sums]


print(Solution().findTargetSumWaysRevise([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
