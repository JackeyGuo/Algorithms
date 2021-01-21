from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        如果最多有 n 个不重叠的区间，那么就至少需要 n 个箭头穿透所有区间

        在最大重叠区间算法中如果两个区间的边界触碰，不算重叠；
        而按照这道题目的描述，箭头如果碰到气球的边界气球也会爆炸，所以说相当于区间的边界触碰也算重叠：
        """
        if not points: return 0

        # 对end进行升序排序
        points.sort(key=lambda k: k[1])

        # 不重叠区间计数器
        count = 1
        x_end = points[0][1]
        for point in points[1:]:
            x_start = point[0]
            # 注意区间边界问题，相等也算重叠区间
            if x_start > x_end:
                # 找到下一个选择的区间了, 计数器+1，end变为赋值新区间的end
                count += 1
                x_end = point[1]

        return count


if __name__ == '__main__':
    print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
