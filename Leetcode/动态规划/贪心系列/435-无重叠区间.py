from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        最大不想交区间：
        从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）。
        把所有与 x 区间相交的区间从区间集合 intvs 中删除。
        重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。

        可以按每个区间的 end 数值升序排序，不难发现所有与 x 相交的区间必然会与 x 的 end 相交；
        如果一个区间不想与 x 的 end 相交，它的 start 必须要大于（或等于）x 的 end
        """
        if not intervals: return 0

        # 对end进行升序排序
        intervals.sort(key=lambda k: k[1])

        # 不重叠区间计数器
        count = 1
        x_end = intervals[0][1]
        for intvs in intervals[1:]:
            x_start = intvs[0]
            if x_start >= x_end:
                # 找到下一个选择的区间了, 计数器+1，end变为赋值新区间的end
                count += 1
                x_end = intvs[1]

        # 剩下的就是至少需要去除的区间吗
        return len(intervals) - count


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
