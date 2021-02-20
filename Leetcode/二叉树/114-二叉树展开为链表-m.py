# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        # 依次寻找到右子树的末端
        while p.right is not None: p = p.right
        # 连接
        p.right = right

