from typing import List
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        重点：
            把每个字符串用二进制数字表示（状态压缩）
            寻找所有子集（subset）

        第一步：状态压缩
            注意题目的第二个条件只要求能找到（出现一次即可），对出现次数没要求。为了解决这个问题，
            我们可以使用二进制数字来表每个 word 和 puzzle，该二进制数字就是 word 和 puzzle 的特征。
            这道题只包含 26 个小写字母，可以压缩到一个 int 中。int 中的每一位取 0 和 1 表示字符是否出现过。
            比如 "aabb" 可以用 11 表示，"accc" 可以用 101 表示。
            可以看出不同的单词可能映射成同一个数字，比如 "aabbb" 和 "ab" 都映射成了 11。这就是状态压缩。
        第二步：匹配
            根据题目的两个条件，puzzle 的第一个字符必须跟 word 的第一个字符相同；word 中每一个字符都要在 puzzle 中找到，
            所以要找的是 word 状态压缩后的数字 和 puzzle[0] + subset(puzzle[1:N - 1]) 状态压缩后的数字相等。
            很多题解都在讨论二进制表示下的 subset 怎么求，我觉得都不好理解，直接做一下「78. 子集」不就得了？暴力求出puzzle[1:N - 1]的所有子集，
            然后计算 puzzle[0] + subset(puzzle[1:N - 1]) 对应的状态。

            题目说了 puzzle 的长度为 7 位，subset(puzzle[1:N - 1]) 的是时间复杂度为 O(2 ^ N) = 2 ^ 6 = 64 次计算，比较快。

            求出 puzzle[0] + subset(puzzle[1:N - 1]) 对应的二进制数字之后，
        """
        freq = Counter()

        for word in words:
            mask = 0
            for c in word:
                # 把单词映射成一个32位的int
                mask |= 1 << (ord(c) - ord("a"))
            freq[mask] += 1

        res = []
        for puzzle in puzzles:
            total = 0
            for perm in self.subset(puzzle[1:]):
                mask = 1 << (ord(puzzle[0]) - ord("a"))
                for c in perm:
                    mask |= 1 << (ord(c) - ord("a"))
                total += freq[mask]
            res.append(total)
        return res

    def subset(self, words) -> List[List[str]]:
        res = [""]
        for i in words:
            res = res + [i + word for word in res]

        return res


print(Solution().findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                                     puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
