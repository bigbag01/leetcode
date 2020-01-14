#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    用栈迭代的方案
    27/27 cases passed (36 ms)
    Your runtime beats 91.08 % of python3 submissions
    Your memory usage beats 17.6 % of python3 submissions (15.2 MB)
    '''
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     stack = []
    #     while head:
    #         stack.append(head.val)
    #         head = head.next
    #     newList = ListNode(stack.pop())
    #     p = newList
    #     while stack:
    #         node = ListNode(stack.pop())
    #         p.next = node
    #         p = node
    #     return newList

    '''
    递归的方案
    27/27 cases passed (40 ms)
    Your runtime beats 80.12 % of python3 submissions
    Your memory usage beats 14.51 % of python3 submissions (18.3 MB)
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nHead,nTail = self.reverse(head)
        return nHead

    def reverse(self,head):
        if not head.next:
            return head,head
        else:
            nHead, nTail = self.reverse(head.next)
            nTail.next = ListNode(head.val)
            nTail = nTail.next
            return nHead,nTail


    '''
    别人的递归写法，优雅！
    '''
    # def reverseList(self,head:ListNode) -> ListNode:
    #     if head.next == None:ß
    #         return head
    #     last = reverse(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return last
    


# @lc code=end

