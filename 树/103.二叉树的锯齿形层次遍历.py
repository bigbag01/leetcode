#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (52.64%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 53.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    '''
    迭代
    Your runtime beats 28.92 % of python3 submissions
    Your memory usage beats 57.49 % of python3 submissions (13.2 MB)
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue,nxt = [root],[]
        res,row = [],[]
        go = True
        while queue:
            cur = queue.pop(0)
            row.append(cur.val)
            if cur.left:
                nxt.append(cur.left)
            if cur.right:
                nxt.append(cur.right)
            if not queue:
                queue = nxt
                nxt = []
                if go:
                    res.append(row)
                else:
                    res.append(row[::-1])
                go = not go
                row = []
        return res
    '''

    '''
    递归
    Your runtime beats 80.72 % of python3 submissions
    Your memory usage beats 57.49 % of python3 submissions (13.2 MB)
    '''
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [] 
        res = []
        def dolevel(node,level):
            if level == len(res):
                res.append([])
            if level % 2:
                res[level].insert(0,node.val)
            else:
                res[level].append(node.val)
            if node.left:
                dolevel(node.left,level+1)
            if node.right:
                dolevel(node.right,level+1)
        dolevel(root,0)

        return res
# @lc code=end

