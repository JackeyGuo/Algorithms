from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.res_se = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None: self.res_se.extend([None, ","])

        self.res_se.extend([root.val, ","])

        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes_list = data.split(",")
        return self.deseri(nodes_list)

    def deseri(self, nodes: List[str]) -> TreeNode:
        if len(nodes) == 0: return

        # 前序遍历位置
        # 列表最左侧就是根节点
        first = nodes.pop(0)
        if first is None: return

        root = TreeNode(int(first))

        root.left = self.deseri(nodes)
        root.right = self.deseri(nodes)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
