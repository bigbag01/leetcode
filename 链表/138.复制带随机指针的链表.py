#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (40.12%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 41.9K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的 深拷贝。 
# 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 示例 4：
# 
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
# 
# 
# 
# 
# 提示：
# 
# 
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。
# 
# 
#

# @lc code=start
"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    '''
    # 用哈希表存储对应节点
    # Your runtime beats 63.95 % of python3 submissions
    # Your memory usage beats 81.37 % of python3 submissions (13.7 MB)
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cHead = Node(head.val)
        nodeMap = {id(head):cHead}
        p = head
        c = cHead
        while p.next:
            p = p.next
            c.next = Node(p.val)
            c = c.next
            nodeMap[id(p)]=c
        p = head
        c = cHead
        while p:
            if p.random:
                node = nodeMap[id(p.random)]
                c.random = node
            p = p.next
            c = c.next
        return cHead    
    '''

    # 将复制的节点放置到前一个节点后，最后提取复制的节点
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        Your runtime beats 29.28 % of python3 submissions
        Your memory usage beats 82.29 % of python3 submissions (13.5 MB)
        '''
        if not head:
            return None
        # 从头复制一遍节点值
        p = head
        while p:
            nxt = p.next
            clone = Node(p.val)
            clone.next = nxt
            p.next = clone
            p = nxt
        
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None
            p = p.next.next

        p = head
        cHead = p.next
        c = cHead
        while p.next.next:
            p = p.next.next
            c.next = p.next
            c = c.next
        return cHead

    
# @lc code=end

