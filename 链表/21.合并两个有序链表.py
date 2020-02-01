#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (58.51%)
# Likes:    831
# Dislikes: 0
# Total Accepted:    172K
# Total Submissions: 290K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        # 思路1
        Your runtime beats 72.97 % of python3 submissions
        Your memory usage beats 56.85 % of python3 submissions (13.1 MB)
        
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        p1,p2 = l1,l2
        mergedHead = ListNode(None)
        merged = mergedHead
        while p1 and p2:
            if p1.val<p2.val:
                merged.next = p1
                merged = merged.next
                p1 = p1.next
            else:
                merged.next = p2
                merged = merged.next
                p2 = p2.next
        if p1:
            merged.next = p1
        if p2:
            merged.next = p2
        return mergedHead.next
        '''
        
        '''
        思路2 递归,简洁且巧妙,不过时间比较慢
        Your runtime beats 6.61 % of python3 submissions
        Your memory usage beats 56.85 % of python3 submissions (13.3 MB)
        '''
        if l1 and l2:
            if l1.val > l2.val:
                l2,l1 = l1,l2
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1 or l2

# @lc code=end

