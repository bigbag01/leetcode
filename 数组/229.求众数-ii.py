#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (41.81%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 23.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: [3]
# 
# 示例 2:
# 
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 【思路1】用哈希表，统计每个元素出现次数，但是空间复杂度为O(n)
        # 【思路2】还是投票算法，遇到两个不同的才-1
        # Your runtime beats 48.98 % of python3 submissions
        # Your memory usage beats 49.85 % of python3 submissions (14.2 MB)
        if not nums:
            return []
        a,b = None,None
        ca,cb = 0,0
        for n in nums:
            if ca == 0 and n!=b:
                a = n
            if cb == 0 and n!=a:
                b = n
            if n == a:
                ca += 1
            elif n == b:
                cb += 1
            else:
                ca -= 1
                cb -= 1
        ca,cb=0,0
        for n in nums:
            if n == a:
                ca+=1
            if n == b:
                cb+=1
        res = []
        if ca>len(nums)/3:res.append(a)
        if cb>len(nums)/3:res.append(b)
        return res
        
# @lc code=end

