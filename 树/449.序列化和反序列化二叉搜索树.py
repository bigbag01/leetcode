#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (49.34%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 5.8K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
# 
# 设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
# 
# 编码的字符串应尽可能紧凑。
# 
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    用前序遍历+中序遍历构造树的方法来构造
    Your runtime beats 71.79 % of python3 submissions
    Your memory usage beats 16.67 % of python3 submissions (17.2 MB)
    '''
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return []
        stack = [root]
        traverse = []
        while stack:
            cur = stack.pop()
            traverse.append(str(cur.val))
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        
        return ','.join(traverse)
        
    
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        vals = list(map(lambda key:int(key),data.split(',')))
        preorder = vals
        inorder = sorted(vals)

        def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
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

        return buildTree(preorder,inorder)
            
            

# Your Codec object will be instantiated and called as such:

# root = TreeNode(5)
# l = TreeNode(3)
# r = TreeNode(7)
# l.left = TreeNode(0)
# r.right = TreeNode(4)
# root.left = l
# root.right = r
# codec = Codec()
# print(codec.serialize(root))
# tree = codec.deserialize(codec.serialize(root))
# print(tree)
# @lc code=end

