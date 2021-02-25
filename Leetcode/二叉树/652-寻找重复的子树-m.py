from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = {}
        self.res = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.traverse(root)
        return self.res

    def traverse(self, root: TreeNode) -> str:
        if not root: return "#"

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        subTree = left + "," + right + "," + str(root.val)

        if subTree not in self.memo.keys():
            self.memo[subTree] = 0
        else:
            self.res.append(root)

        return subTree