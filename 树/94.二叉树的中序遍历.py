#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (69.02%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    92.9K
# Total Submissions: 133.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    Your runtime beats 87.12 % of python3 submissions
    Your memory usage beats 23.72 % of python3 submissions (13.2 MB)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val,]+self.inorderTraversal(root.right)
    '''

    '''
    迭代
    每次父节点删去left压栈，然后前进到左子节点，如果当前没有左子节点，就输出，如果当前有右子节点，就压栈。
    Your runtime beats 95.29 % of python3 submissions
    Your memory usage beats 6.06 % of python3 submissions (13.3 MB)
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        traverse = []
        cur = root
        while True:
            if cur.left:
                rcur = cur
                cur = cur.left
                rcur.left = None
                stack.append(rcur)
            else:
                traverse.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if not stack:
                    break
                cur = stack.pop()
        return traverse

# @lc code=end

