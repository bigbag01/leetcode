#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (62.77%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 59.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    Your runtime beats 75.28 % of python3 submissions
    Your memory usage beats 72.23 % of python3 submissions (87 MB)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder)>1:
            index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1+index],inorder[:index])
            root.right = self.buildTree(preorder[1+index:],inorder[1+index:])
        return root
    '''

    '''
    迭代 
    Your runtime beats 100 % of python3 submissions
    Your memory usage beats 99.07 % of python3 submissions (13.9 MB)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        
        p,i = 0,0
        cur = root
        traveled = {}
        while p < len(preorder)-1 and i < len(inorder):
            pre = cur
            if preorder[p]!=inorder[i]:
                if cur.val not in traveled:
                    cur.left = TreeNode(preorder[p+1])
                    cur = cur.left
                else:
                    cur.right = TreeNode(preorder[p+1])
                    cur = cur.right
                p += 1
            else:
                if i + 1 == len(inorder):break
                while inorder[i+1] in traveled:
                    cur = traveled[inorder[i+1]]
                    i += 1
                i += 1
            traveled[pre.val] = pre
        return root                    





# @lc code=end

