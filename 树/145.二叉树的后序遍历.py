#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (68.83%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    45.4K
# Total Submissions: 65.3K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    Your runtime beats 54.55 % of python3 submissions
    Your memory usage beats 12.47 % of python3 submissions (13.3 MB)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val,]
    '''


    '''
    迭代
    Your runtime beats 36.85 % of python3 submissions
    Your memory usage beats 11.4 % of python3 submissions (13.3 MB)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur = root
        stack = [cur,]
        traverse = []
        passby=set()
        while cur!=None and len(stack)>0:
            if (not cur.left and not cur.right) or cur in passby:
                traverse.append(cur.val)
            else:
                passby.add(cur)
                stack.append(cur)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            cur = stack.pop()
        return traverse
    '''

    '''
    迭代优化写法，参考leetcode题解
    Your runtime beats 95.62 % of python3 submissions
    Your memory usage beats 95.27 % of python3 submissions (13 MB)
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        traverse = []
        while stack:
            cur = stack.pop()
            traverse.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return traverse[::-1]
    
# @lc code=end

