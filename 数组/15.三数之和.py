#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.57%)
# Likes:    1711
# Dislikes: 0
# Total Accepted:    143.8K
# Total Submissions: 573.3K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        registry = {}
        result = []
        for i in range(len(nums)):
            n = nums[i]
            if n in registry:
                registry[n] = (registry[n][0],registry[n][0]+1)
            else:
                registry[n] = (i,i)
        for key in registry:
            a = key
            i,j = registry[key][0]+1,len(nums)-1
            while i<j:
                b = nums[i]
                c = nums[j]
                cur_sum = a+b+c
                if cur_sum == 0:
                    result.append([a,b,c])
                    while i<j and nums[i] == b:
                        i += 1
                    while i<j and nums[j] == c:
                        j -=1
                elif cur_sum > 0:
                    while j>i and nums[j]==c:
                        j-=1
                else:
                    while i<j and nums[i]==b:
                        i+=1
        return result
# @lc code=end

