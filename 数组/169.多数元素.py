#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (60.65%)
# Likes:    422
# Dislikes: 0
# Total Accepted:    102.7K
# Total Submissions: 167.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 【解法1】
        '''
        时间O(nlon)，空间O(logn) 如果是快排
        排序，中间那个一定是中位数的
        Your runtime beats 87.7 % of python3 submissions
        Your memory usage beats 57.23 % of python3 submissions (14.4 MB)
        nums.sort()
        return nums[len(nums)>>1]
        '''

        # 【解法2】
        '''
        O(1)空间，O(N)时间
        Your runtime beats 5.6 % of python3 submissions
        Your memory usage beats 56.97 % of python3 submissions (14.5 MB)
        
        if len(nums)==1:
            return nums[0]
        i,j = 0,1
        cand = nums[i]
        while i<len(nums)-1 and j<len(nums):
            if nums[i]!=nums[j]:
                nums[i] = None
                nums[j] = None
            while i<len(nums)-1 and nums[i]==None:
                i += 1
            j = max(i+1,j)
            while j<len(nums) and (nums[j]==None or nums[j]==nums[i]):
                j+=1
        return nums[i]
        '''

        # 【解法3】
        '''
        参考题解对解法2进行优化
        Boyer-Moore 投票算法
        Your runtime beats 5.04 % of python3 submissions
        Your memory usage beats 56.79 % of python3 submissions (14.6 MB)
        '''
        cand = nums[0]
        cnt = 0
        for n in nums:
            if cnt == 0:
                cand = n
            cnt += 1 if (cand==n) else -1

        return cand
# @lc code=end

