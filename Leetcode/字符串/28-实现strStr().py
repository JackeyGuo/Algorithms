class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        最直接的方法 - 沿着字符换逐步移动滑动窗口，将窗口内的子串与 needle 字符串比较。
        """
        n = len(haystack)
        m = len(needle)

        # 只需要对比到n-m+1位置即可
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().strStr("aaaaa", ""))
