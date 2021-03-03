# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        对数据结构的操作无非遍历 + 访问，遍历就是「找」，访问就是「改」。
        具体到这个问题，插入一个数，就是先找到插入位置，然后进行插入操作。
        上一个查找问题，总结了 BST 中的遍历框架，就是「找」的问题。
        直接套框架，加上「改」的操作即可。一旦涉及「改」，函数就要返回TreeNode类型，并且对递归调用的返回值进行接收。
        """
        if root is None: return TreeNode(val)
        # if (root.val == val)
        # BST 中一般不会插入已存在元素
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
