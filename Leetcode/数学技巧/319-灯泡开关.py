import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == "__main__":
    solution = Solution()
    print(solution.bulbSwitch(3))