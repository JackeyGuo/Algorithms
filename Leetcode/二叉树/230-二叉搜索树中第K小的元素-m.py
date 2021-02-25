# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        直接的思路就是升序排序，然后找第k个元素。BST(二叉搜索树) 的中序遍历其实就是升序排序的结果
        """
        self.res, self.rank = 0, 0

        def traverse(root: TreeNode):
            if not root: return

            traverse(root.left)

            # 中序遍历代码位置
            self.rank += 1
            if self.rank == k:
                self.res = root.val
                return
            traverse(root.right)

        traverse(root)
        return self.res

    """
    优化方案：将时间复杂度降到 O(logN)
    
    查找排名为 k 的元素，当前节点知道自己排名第 m ，那么我可以比较 m 和 k 的大小：

    1、如果 m == k，显然就是找到了第 k 个元素，返回当前节点就行了。
    
    2、如果 k < m，那说明排名第 k 的元素在左子树，所以可以去左子树搜索第 k 个元素。
    
    3、如果 k > m，那说明排名第 k 的元素在右子树，所以可以去右子树搜索第 k - m - 1个元素。
    
    需要在二叉树节点中维护额外信息。每个节点需要记录，以自己为根的这棵二叉树有多少个节点。

    也就是说，我们TreeNode中的字段应该如下：
    
    class TreeNode {
        int val;
        // 以该节点为根的树的节点总数
        int size;
        TreeNode left;
        TreeNode right;
    }
    
    有了size字段，外加 BST 节点左小右大的性质，对于每个节点node就可以通过node.left推导出node的排名，从而做到对数级算法，
    size字段需要在增删元素的时候需要被正确维护
    """


from typing import List


class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def traverse(root: TreeNode) -> List[int]:
            # 一点奇淫巧计
            return traverse(root.left) + [root.val] + traverse(root.right) if root else []

        return traverse(root)[k - 1]
