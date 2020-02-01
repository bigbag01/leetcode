#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (75.46%)
# Likes:    448
# Dislikes: 0
# Total Accepted:    56.1K
# Total Submissions: 73.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    '''
    迭代
    Your runtime beats 91.27 % of python3 submissions
    Your memory usage beats 52.96 % of python3 submissions (13.3 MB)
    def subsets(self, nums):
        res = []
        for i in range(len(nums)):
            cur = []
            cur.append([nums[i]])
            for sub in res:
                cur.append(sub+[nums[i]])
            res = res + cur
        res.append([])
        return res
    '''

    '''
    位运算
    Your runtime beats 79.63 % of python3 submissions
    Your memory usage beats 52.96 % of python3 submissions (13.2 MB)
    '''
    def subsets(self,nums):
        res = []
        for i in range(1<<len(nums)):
            cur = []
            for j in range(len(nums)):
                if (i >> j) & 1 == 1 :
                    cur.append(nums[j])
            res.append(cur)
        return res
        
# @lc code=end

sol = Solution()
print(sol.subsets([1,2,3,4]))