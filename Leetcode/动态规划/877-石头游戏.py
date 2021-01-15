from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 控制自己拿到所有偶数堆，或者所有的奇数堆，选择奇数堆和偶数堆石头总数多的，就能赢
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGame([5, 3, 4, 5]))
