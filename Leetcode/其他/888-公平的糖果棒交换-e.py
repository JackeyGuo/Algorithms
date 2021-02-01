from typing import List
import collections


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # 数学+哈希表
        sumA, sumB = sum(A), sum(B)
        dic = set(A)

        diff = int((sumA - sumB) / 2)
        for b in B:
            a = diff + b
            if a in dic:
                return [a, b]


print(Solution().fairCandySwap(A=[1, 2, 5], B=[2, 4]))
