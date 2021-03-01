# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 记录累加和
        self.res = 0
        self.traverse(root)
        return root

    def traverse(self, root: TreeNode):
        if not root: return
        # 降序打印节点的值
        self.traverse(root.right)
        # 维护累加和
        self.res += root.val
        # 将 BST 转化成累加树
        root.val = self.res

        self.traverse(root.left)
