# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if root is None: return

        if root.val == key:
            # 情况一：末端节点，两个子节点都为空
            # 情况二：只有一个非空子节点，那么它要让这个孩子接替自己的位置
            # 这两个 if 把情况 1 和 2 都正确处理了
            if root.left is None: return root.right
            if root.right is None: return root.left
            # 情况三：左右子树都存在，找右子树中的最小值替代该节点
            # 找到右子树的最小节点
            minNode = self.getMin(root.right)
            # 把 root 改成 minNode
            root.val = minNode.val
            # 转而去删除 minNode
            root.right = self.deleteNode(root.right, minNode.val)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        # BST 最左节点就是最小的节点
        while node.left is not None: node = node.left
        return node

    # 注意一下，这个删除操作并不完美，因为我们一般不会通过root.val = minNode.val修改节点内部的值来交换节点，而是通过一系列略微复杂的链表操作交换root和minNode两个节点。
    # 因为具体应用中，val域可能会是一个复杂的数据结构，修改起来非常麻烦；而链表操作无非改一改指针，而不会去碰内部数据。