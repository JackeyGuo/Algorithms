# 滑动窗口算法框架
"""
滑动窗口算法的思路是这样：

1、我们在字符串S中使用双指针中的左右指针技巧，初始化left = right = 0，把索引左闭右开区间[left, right)称为一个「窗口」。

2、我们先不断地增加right指针扩大窗口[left, right)，直到窗口中的字符串符合要求（包含了T中的所有字符）。

3、此时，我们停止增加right，转而不断增加left指针缩小窗口[left, right)，直到窗口中的字符串不再符合要求（不包含T中的所有字符了）。同时，每次增加left，我们都要更新一轮结果。

4、重复第 2 和第 3 步，直到right到达字符串S的尽头。
"""

"""
现在开始套模板，只需要思考以下四个问题：

1、当移动right扩大窗口，即加入字符时，应该更新哪些数据？

2、什么条件下，窗口应该暂停扩大，开始移动left缩小窗口？

3、当移动left缩小窗口，即移出字符时，应该更新哪些数据？

4、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？

如果一个字符进入窗口，应该增加window计数器；如果一个字符将移出窗口的时候，应该减少window计数器；
当valid满足need时应该收缩窗口；应该在收缩窗口的时候更新最终结果。

"""
class Solution:
    def slidingWindow(self, s: str, t: str) -> str:
        # 创建 哈希表（字典）
        # 将字典中所有键的值初始化为0
        needs = {}.fromkeys(t, 0)
        windows = {}.fromkeys(t, 0)
        # 记录所需字符的个数
        for c in t: needs[c] += 1

        # valid 变量表示窗口中满足 need 条件的字符个数
        # 如果 valid 和 need 的大小相同，则说明窗口已满足条件，已经完全覆盖了串T
        left, right, valid = 0, 0, 0
        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            '''......'''

            # debug 输出的位置
            print("window: [%d, %d)" % (left, right))

            # 判断左侧窗口是否要收缩
            while ("window needs shrink"):
                # d 是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 进行窗口内数据的一系列更新
                '''......'''

    # 两个...处的操作分别是右移和左移窗口更新操作

print(Solution().slidingWindow(s = "ADOBECODEBANC", t = "ABC"))