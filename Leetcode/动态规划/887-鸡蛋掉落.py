class Solution:
    """
    带有两个状态参数的 dp 函数来表示状态转移；外加一个 for 循环来遍历所有选择，择最优的选择更新状态
    """

    def superEggDrop(self, K: int, N: int) -> int:
        # 带备忘录，消除重叠子问题
        memo = dict()

        # 当前状态为 K 个鸡蛋，面对 N 层楼
        # 返回这个状态下的最优结果
        def dp(K, N):
            # base case
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 最坏情况下的最少扔鸡蛋次数
            for i in range(1, N + 1):
                # 最坏情况下扔鸡蛋的次数，所以鸡蛋在第 i 层楼碎没碎，取决于那种情况的结果更大
                res = min(res,
                          max(
                              dp(K - 1, i - 1),  # 碎
                              dp(K, N - i)  # 没碎
                          ) + 1  # 在第 i 楼扔了一次
                          )
            # 计入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)

    # 二分搜索替代线性扫描，提高搜索效率
    def superEggDrop_new(self, K: int, N: int) -> int:
        # 带备忘录，消除重叠子问题
        memo = dict()

        # 当前状态为 K 个鸡蛋，面对 N 层楼
        # 返回这个状态下的最优结果
        def dp(K, N):
            # base case
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 用二分搜索代替线性搜索
            low, high = 1, N
            while low <= high:
                mid = (low + high) // 2  # 相当于 i 楼层
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)
            # 计入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)


if __name__ == "__main__":
    solution = Solution()
    print(solution.superEggDrop(3, 14))
