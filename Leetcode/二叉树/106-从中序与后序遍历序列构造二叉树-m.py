from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(postorder, 0, len(postorder) - 1,
                          inorder, 0, len(inorder) - 1)

    def build(self, postorder, postStart, postEnd, inorder, inStart, inEnd) -> TreeNode:
        if inStart > inEnd: return

        # root 节点对应的值就是后序遍历数组的最后一个元素
        rootVal = postorder[postEnd]
        # rootVal 在中序遍历数组中的索引
        index = inorder.index(rootVal)

        # 计算出根节点左子树的节点个数
        leftSize = index - inStart
        # 先构造出当前根节点
        root = TreeNode(rootVal)
        # 递归构造左右子树
        root.left = self.build(postorder, postStart, postStart + leftSize - 1,
                               inorder, inStart, index - 1)
        root.right = self.build(postorder, postStart + leftSize, postEnd - 1,
                                inorder, index + 1, inEnd)

        return root


print(Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
