# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        通过使用辅助函数，增加函数参数列表，在参数中携带额外信息，将这种约束传递给子树的所有节点
        """
        return self.validBST(root, None, None)

    # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
    def validBST(self, root: TreeNode, minNode: TreeNode, maxNode: TreeNode):
        # base case
        if root is None: return True
        # 若 root.val 不符合 max 和 min 的限制，说明不是合法的 BST
        if minNode is not None and root.val <= minNode.val: return False
        if maxNode is not None and root.val >= maxNode.val: return False

        return self.validBST(root.left, minNode, root) and \
               self.validBST(root.right, root, maxNode)