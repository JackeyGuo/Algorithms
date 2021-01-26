from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        # 暴力法方案-超时
        # count = 0
        # for i in range(len(dominoes)):
        #     for j in range(i + 1, len(dominoes)):
        #         if ((dominoes[i][0] == dominoes[j][0]) and (dominoes[i][1] == dominoes[j][1])) or \
        #                 ((dominoes[i][1] == dominoes[j][0]) and (dominoes[i][0] == dominoes[j][1])):
        #             count += 1

        # 先排序，然后使用哈希字典记录 list 的出现次数，最后累加
        count = 0
        dict = {}
        for d1, d2 in dominoes:
            # 排序后加入字典
            sd = tuple(sorted((d1, d2)))
            if sd not in dict:
                dict[sd] = 1
            else:
                dict[sd] += 1

        for k, v in dict.items():
            count += v * (v - 1) / 2

        return int(count)


print(Solution().numEquivDominoPairs(
    [[2, 1], [5, 4], [3, 7], [6, 2], [4, 4], [1, 8], [9, 6], [5, 3], [7, 4], [1, 9], [1, 1], [6, 6], [9, 6], [1, 3],
     [9, 7], [4, 7], [5, 1], [6, 5], [1, 6], [6, 1], [1, 8], [7, 2], [2, 4], [1, 6], [3, 1], [3, 9], [3, 7], [9, 1],
     [1, 9], [8, 9]]))
