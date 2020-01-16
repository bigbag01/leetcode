#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (59.83%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    70.1K
# Total Submissions: 116.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
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
    Your runtime beats 76.28 % of python3 submissions
    Your memory usage beats 63.42 % of python3 submissions (13.4 MB)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        res = []
        while True:
            nxt_queue=[]
            row = []
            while queue:
                cur = queue.pop(0)
                row.append(cur.val)
                if cur.left:
                    nxt_queue.append(cur.left)
                if cur.right:
                    nxt_queue.append(cur.right)
            queue = nxt_queue
            res.append(row)
            if not nxt_queue:
                break
        return res
    '''

    '''
    参考官方题解做的递归解法
    Your runtime beats 98.65 % of python3 submissions
    Your memory usage beats 9.73 % of python3 submissions (13.9 MB)
    '''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        def helper(node, level):
            # 每层第一个，先加一个空数组进去
            if level == len(res):
                res.append([])
            # 添加当前节点到对应层
            res[level].append(node.val)
            # 子节点是下一层
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)

        helper(root,0)
        return res

# @lc code=end

