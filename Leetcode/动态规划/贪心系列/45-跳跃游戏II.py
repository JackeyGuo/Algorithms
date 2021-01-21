from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        选择可跳跃区域涵盖了索引区间的最大值
        贪心选择性质，我们不需要【递归地】计算出所有选择的具体结果然后比较求最值，而只需要做出那个最有【潜力】，看起来最优的选择即可
        """
        n = len(nums)

        farthest, jumps, end = 0, 0, 0
        # 不访问最后一个元素，因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            # 维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。
            if end == i:
                jumps += 1
                end = farthest

        return jumps


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 2, 4, 2, 3]))
