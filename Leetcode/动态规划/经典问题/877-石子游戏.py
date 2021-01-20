from typing import List

"""
参考labuladong方案，改为Python代码
"""


class Solution:
    """
    使用二维dp数组存储dict(fir, sec)，含义：
    dp[i][j].fir 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数。
    dp[i][j].sec 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数。

    举例理解一下，假设 piles = [3, 9, 1, 2]，索引从 0 开始
    dp[0][1].fir = 9 意味着：面对石头堆 [3, 9]，先手最终能够获得 9 分。
    dp[1][3].sec = 2 意味着：面对石头堆 [9, 1, 2]，后手最终能够获得 2 分。

    想求的答案是先手和后手最终分数之差，按照这个定义也就是 dp[0][n-1].fir - dp[0][n-1].sec，
    即面对整个 piles，先手的最优得分和后手的最优得分之差。

    状态显然有三个：开始的索引 i，结束的索引 j，当前轮到的人
    dp[i][j][fir or sec]
    其中：
    0 <= i < piles.length
    i <= j < piles.length

    状态转移方程：
    dp[i][j].fir = max(piles[i] + dp[i+1][j].sec, piles[j] + dp[i][j-1].sec)
    dp[i][j].fir = max(    选择最左边的石头堆     ,     选择最右边的石头堆     )
    # 解释：我作为先手，面对 piles[i...j] 时，有两种选择：
    # 要么我选择最左边的那一堆石头，然后面对 piles[i+1...j]
    # 但是此时轮到对方，相当于我变成了后手；
    # 要么我选择最右边的那一堆石头，然后面对 piles[i...j-1]
    # 但是此时轮到对方，相当于我变成了后手。

    if 先手选择左边:
        dp[i][j].sec = dp[i+1][j].fir
    if 先手选择右边:
        dp[i][j].sec = dp[i][j-1].fir
    # 解释：我作为后手，要等先手先选择，有两种情况：
    # 如果先手选择了最左边那堆，给我剩下了 piles[i+1...j]
    # 此时轮到我，我变成了先手；
    # 如果先手选择了最右边那堆，给我剩下了 piles[i...j-1]
    # 此时轮到我，我变成了先手。

    base case：
    dp[i][j].fir = piles[i]
    dp[i][j].sec = 0
    其中 0 <= i == j < n
    # 解释：i 和 j 相等就是说面前只有一堆石头 piles[i]
    # 那么显然先手的得分为 piles[i]
    # 后手没有石头拿了，得分为 0

    推算 dp[i][j] 时需要用到 dp[i+1][j] 和 dp[i][j-1]，所以需要斜着遍历数组。

    """

    # 返回游戏最后先手和后手的得分之差
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[0, 0]] * n for _ in range(n)]

        # 处理base case
        for i in range(n):
            dp[i][i] = [piles[i], 0]

        # 斜着遍历数组
        """
        (0,1),(1,2),(2,3)
        (0,2),(1,3)
        (0,3)
        """
        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = l + i - 1
                # 先手选择最左边或最右边的分数
                left = piles[i] + dp[i + 1][j][1]
                right = piles[j] + dp[i][j - 1][1]

                # 套用状态转移方程
                if left > right:
                    dp[i][j] = [left, dp[i + 1][j][0]]
                else:
                    dp[i][j] = [right, dp[i][j - 1][0]]

        # 返回游戏最后先手和后手的得分之差,先手大，先手赢，后手大后手赢
        return (dp[0][n - 1][0] - dp[0][n - 1][1]) >= 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGame([5, 3, 4, 5]))
