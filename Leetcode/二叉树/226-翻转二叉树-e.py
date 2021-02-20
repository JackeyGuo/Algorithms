"""
只要把二叉树上的每一个节点的左右子节点进行交换，最后的结果就是完全翻转之后的二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root: return None

        # /**** 前序遍历位置 ****/
        # root 节点需要交换它的左右子节点
        tmp = root.left
        root.left = root.right
        root.right = tmp.left

        # 让左右子节点继续翻转它们的子节点
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
