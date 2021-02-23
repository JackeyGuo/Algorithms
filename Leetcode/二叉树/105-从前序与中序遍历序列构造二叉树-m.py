from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1)

    # 若前序遍历数组为 preorder[preStart..preEnd]，
    # 后续遍历数组为 postorder[postStart..postEnd]，
    # 构造二叉树，返回该二叉树的根节点
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd) -> TreeNode:
        if preStart > preEnd: return

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # rootVal 在中序遍历数组中的索引
        index = inorder.index(rootVal)

        # 计算出根节点左子树的节点个数
        leftSize = index - inStart
        # 先构造出当前根节点
        root = TreeNode(rootVal)
        # 递归构造左右子树
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)

        return root


print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
