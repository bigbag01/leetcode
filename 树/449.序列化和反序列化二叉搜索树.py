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
    解法一
    按层次遍历思想迭代，没有考虑二叉搜索树的特点
    Your runtime beats 18.42 % of python3 submissions
    Your memory usage beats 16.67 % of python3 submissions (17.1 MB)
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        res = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('#')
        return ','.join(res)
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = [root]
        nodes.pop(0)
        while nodes:
            parent = queue.pop(0)
            l = nodes.pop(0)
            r = nodes.pop(0)
            if l != '#':
                parent.left = TreeNode(int(l))
                queue.append(parent.left)
            if r != '#':
                parent.right = TreeNode(int(r))
                queue.append(parent.right)
        return root
    '''

    '''
    解法二 按先序遍历的思路迭代 
    Your runtime beats 23.68 % of python3 submissions
    Your memory usage beats 16.67 % of python3 submissions (17.2 MB)
    '''
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return '#'
        return '%s,%s,%s' % (root.val,self.serialize(root.left),self.serialize(root.right))
        
    
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        nodes = data.split(',')

        def helper(nodes):
            if nodes[0] == '#':
                nodes.pop(0)
                return None
            else:
                val = int(nodes.pop(0))
                cur = TreeNode(val)
                cur.left = helper(nodes)
                cur.right = helper(nodes)
                return cur
        return helper(nodes)

# Your Codec object will be instantiated and called as such:
# root = TreeNode(5)
# l = TreeNode(3)
# r = TreeNode(4)
# l.left = TreeNode(0)
# r.right = TreeNode(7)
# root.left = l
# root.right = r
# codec = Codec()
# tree = codec.deserialize(codec.serialize(root))
# print(tree)
# @lc code=end

