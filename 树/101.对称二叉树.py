#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.14%)
# Likes:    570
# Dislikes: 0
# Total Accepted:    84.4K
# Total Submissions: 170.5K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    Your runtime beats 87.09 % of python3 submissions
    Your memory usage beats 6.56 % of python3 submissions (13.3 MB)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def checkMirror(n1,n2):
            if (n1 == None and n2 != None) or (n1 != None and n2 == None):
                return False
            if n1 == None and n2 ==None:
                return True  
            if not n1.left and not n1.right and not n2.left and not n2.right:
                return n1.val == n2.val
            else:
                return checkMirror(n1.left,n2.right) and checkMirror(n1.right,n2.left) and n1.val == n2.val
        
        return checkMirror(root.left,root.right)
    '''            
            
    '''
    迭代
    Your runtime beats 38.69 % of python3 submissions
    Your memory usage beats 76.5 % of python3 submissions (13.1 MB)
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left = [root.left]
        right = [root.right]
        while left and right and len(left)==len(right):
            lcur = left.pop(0)
            rcur = right.pop(0)
            if not lcur and not rcur:
                continue
            if lcur and rcur and lcur.val == rcur.val:
                left.append(lcur.left)
                left.append(lcur.right)
                right.append(rcur.right)
                right.append(rcur.left)
            else:
                return False
        if not left and not right:
            return True
        else:
            return False

# @lc code=end

