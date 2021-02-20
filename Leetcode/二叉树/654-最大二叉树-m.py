from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        先明确根节点做什么？对于构造二叉树的问题，根节点要做的就是把想办法把自己构造出来
        """
        # base case
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])

        # 第一步：先找数组中的最大值和索引
        max_value = max(nums)
        index = nums.index(max_value)

        # 创建根节点
        root = TreeNode(max_value)
        # 递归调用构造左右子树
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root


print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
