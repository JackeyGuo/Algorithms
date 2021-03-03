# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root is None: return None
        # 找到了返回根节点
        if root.val == val: return root
        # 类似二分查找思想：当前节点没找到就递归地去左右子树寻找
        if root.val < val: return self.searchBST(root.right, val)
        if root.val > val: return self.searchBST(root.left, val)
