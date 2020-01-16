#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (62.63%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    60.7K
# Total Submissions: 95.7K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    '''
    递归
    68/68 cases passed (36 ms)
    Your runtime beats 70.75 % of python3 submissions
    Your memory usage beats 41.48 % of python3 submissions (13.2 MB)
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
    '''
    
    '''
    迭代
    68/68 cases passed (36 ms)
    Your runtime beats 70.75 % of python3 submissions
    Your memory usage beats 52.59 % of python3 submissions (13.1 MB)
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        traverse = []
        while stack:
            cur = stack.pop()
            traverse.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return traverse
# @lc code=end

