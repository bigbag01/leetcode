#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (72.83%)
# Likes:    508
# Dislikes: 0
# Total Accepted:    71.8K
# Total Submissions: 97.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 73.91 % of python3 submissions
    Your memory usage beats 58.94 % of python3 submissions (13.2 MB)
    '''
    def permute(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+perm)
        return res
# @lc code=end

