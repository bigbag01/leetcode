#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    迭代解法
    44/44 cases passed (44 ms)
    Your runtime beats 39.91 % of python3 submissions
    Your memory usage beats 70.98 % of python3 submissions (13.1 MB)
    '''
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        vHead = ListNode(None)
        vHead.next = head
        cnt = 0
        p = vHead
        start,middle,end = [None,None,None]
        while p:
            if cnt == m-1:
                start = p
            if cnt == m:
                middle = p
            if cnt == n:
                end = p.next
                p.next = None
            p = p.next
            cnt += 1
        stack = []
        while middle:
            stack.append(middle.val)
            middle = middle.next
        rev = ListNode(stack.pop())
        pp = rev
        while stack:
            node = ListNode(stack.pop())
            pp.next = node
            pp = node
        start.next = rev
        pp.next = end
        return vHead.next


# @lc code=end

