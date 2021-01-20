class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树问题，后续再继续改进
class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0  # 偷，不偷

            left = _rob(root.left)
            right = _rob(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            v2 = max(left) + max(right)
            return v1, v2

        return max(_rob(root))


if __name__ == "__main__":
    print(Solution.rob([3,2,3,null,3,null,1]))
