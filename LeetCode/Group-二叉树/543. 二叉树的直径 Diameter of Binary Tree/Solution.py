# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            # 更新外层的diameter计数
            nonlocal diameter
            if not node:
                return 0

            # 递归计算左右子树的深度
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            diameter = max(diameter, left_depth + right_depth)

            # 当前node的深度是左右两个子node深度最大值+1
            current_level = max(left_depth, right_depth) + 1
            return current_level
        
        dfs(root)
        return diameter