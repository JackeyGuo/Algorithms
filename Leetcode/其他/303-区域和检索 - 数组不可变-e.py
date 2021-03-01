from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        """
        一次累加计算，多次调用 sumRange 以减少时间复杂度
        """
        self.sumList = [0]
        for i in range(len(nums)):
            self.sumList.append(self.sumList[i] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.sumList[j + 1] - self.sumList[i]
