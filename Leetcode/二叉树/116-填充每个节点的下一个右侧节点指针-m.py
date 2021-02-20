# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 方法一：递归
    def connect(self, root: 'Node') -> Node:
        if not root: return
        self.connectTwoNode(root.left, root.right)

        return root

    def connectTwoNode(self, node1: 'Node', node2: 'Node'):
        """
        输入两个节点，将它俩连接起来
        """
        if not node1 or not node2: return

        # **** 前序遍历位置 ****/
        # 将传入的两个节点连接
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)

        # 连接跨越父节点的两个子节点
        self.connectTwoNode(node1.right, node2.left)

    # 方法二：层次遍历（队列）
    def connect2(self, root: 'Node') -> Node:
        import collections

        if not root: return

        # 初始化队列同时将第一层节点加入队列中，即根节点
        que = collections.deque([root])
        # 外层的 while 循环迭代的是层数
        while que:
            # 记录当前队列的大小
            size = len(que)

            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node = que.popleft()

                # 连接
                if i < size - 1:
                    node.next = que[0]

                # 拓展下一层节点
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

        return root