from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        每一步都计算一下从当前位置最远能够跳到哪里，然后和一个全局最优的最远位置 farthest 做对比，通过每一步的最优解，更新全局最优解，这就是贪心。
        """
        n = len(nums)
        if n == 1: return True

        farthest = 0
        # 第0个位置不需要跳，实际跳的次数为 n-1, 到达最后一个位置
        for i in range(n - 1):
            # 不断计算能跳到的最远距离，当前能跳最远的距离+跳到自己这个位置需要的距离
            farthest = max(farthest, i + nums[i])
            # 当 farthest<i ，说明无法跳到 i 这个位置，等于 i ，说明只能跳到 i 这个位置
            # 可能碰到了 0，卡住跳不动了，最远距离必须大于当前位置距离
            if farthest <= i: return False
        # 判断 farthest 是否大于等于n-1
        return farthest >= n - 1


if __name__ == '__main__':
    print(Solution().canJump([2, 0, 0]))
