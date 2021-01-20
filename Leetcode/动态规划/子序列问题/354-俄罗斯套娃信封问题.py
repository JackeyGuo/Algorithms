from typing import List


class Solution:
    # envelopes = [[w, h], [w, h]...]
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序。
        之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案。
        因为两个宽度相同的信封不能相互包含的，逆序排序保证在 w 相同的数对中最多只选取一个.
        """
        n = len(envelopes)
        if not envelopes: return 0
        # 按宽度升序排列，如果宽度一样，则按高度降序排列, 第一维升序，第二维降序
        envelopes.sort(key=lambda k: (k[0], -k[1]))

        # 取二维数组第二列
        nums = [enve[1] for enve in envelopes]

        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    print(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
