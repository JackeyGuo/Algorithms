from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        先计算不使用秘密技巧下的顾客总数，然后通过固定滑动窗口计算使用秘密技巧下的顾客总数
        """
        n, total = len(customers), 0
        # 计算不使用秘密技巧下的顾客总数
        for i in range(n):
            if not grumpy[i]:
                total += customers[i]

        # 先计算起始的 [0, X) 区间
        curValue = 0
        for i in range(X):
            if grumpy[i] == 1:
                curValue += customers[i]

        resValue = curValue
        # 然后利用滑动窗口，每次向右移动一步
        for i in range(X, n):
            # 如果新进入窗口的元素是生气的，累加不满意的顾客到滑动窗口中
            if grumpy[i] == 1:
                curValue += customers[i]
            # 如果离开窗口的元素是生气的，则从滑动窗口中减去该不满意的顾客数
            if grumpy[i - X] == 1:
                curValue -= customers[i - X]
            # 求所有窗口内不满意顾客的最大值
            resValue = max(resValue, curValue)
        # 最终结果是：不生气时的顾客总数 + 窗口X内挽留的因为生气被赶走的顾客数
        return total + resValue


print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))
