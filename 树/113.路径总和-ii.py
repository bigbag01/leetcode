#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (57.81%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 44.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return []
        root.parent = None
        stack = [root]
        total_stack = [root.val]
        paths = []
        while stack:
            cur = stack.pop()
            total = total_stack.pop()
            if total == sum and self.isLeaf(cur):
                p = cur
                path = []
                while p:
                    path.append(p.val)
                    p = p.parent
                paths.append(path[::-1])
            if cur.left:
                cur.left.parent = cur
                tmp = total+cur.left.val
                stack.append(cur.left)
                total_stack.append(tmp)
            if cur.right:
                cur.right.parent = cur
                tmp = total + cur.right.val
                stack.append(cur.right)
                total_stack.append(tmp)
        return paths


    def isLeaf(self, node):
        return (not node.left and not node.right)
# @lc code=end

