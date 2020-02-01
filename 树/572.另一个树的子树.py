#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#
# https://leetcode-cn.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (42.08%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    12.3K
# Total Submissions: 28.9K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s
# 也可以看做它自身的一棵子树。
# 
# 示例 1:
# 给定的树 s:
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# 
# 给定的树 t：
# 
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# 
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
# 
# 示例 2:
# 给定的树 s：
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# 
# 给定的树 t：
# 
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# 
# 返回 false。
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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''
        Your runtime beats 70.19 % of python3 submissions
        Your memory usage beats 47.29 % of python3 submissions (14.2 MB)
        '''
        if not s:
            return not t
        if not t:
            return False
        def checkEqual(a,b):
            if a and b:
                return a.val==b.val and checkEqual(a.left,b.left) and checkEqual(a.right,b.right)
            else:
                return not a and not b
        if s.val == t.val and checkEqual(s.left,t.left) and checkEqual(s.right,t.right):
                return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

        
# @lc code=end

