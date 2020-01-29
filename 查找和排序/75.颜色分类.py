#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (53.87%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    52.9K
# Total Submissions: 97.3K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 
# 示例:
# 
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 
# 进阶：
# 
# 
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两趟扫描就不写了
        # 一趟扫描，用三个指针管理三个数
        # Your runtime beats 89.06 % of python3 submissions
        # Your memory usage beats 57.44 % of python3 submissions (13 MB)
        if len(nums)==1:
            return
        if len(nums)==2:
            if nums[1]<nums[0]:
                nums[0],nums[1] = nums[1],nums[0]
            return
        
        h,t,m = 0,len(nums)-1,1
        while h<=t and m<=t:
            m = max(m,h)
            if nums[m] > nums[t]:
                nums[m],nums[t]=nums[t],nums[m]
            if nums[m] < nums[h]:
                nums[h],nums[m]=nums[m],nums[h] 
            else:
                m+=1
            while h<len(nums) and nums[h]==0:
                h += 1
            while t>=0 and nums[t]==2:
                t -= 1
        return 
        
# @lc code=end

sol = Solution()
nums = [1,2,2,2,2,0,0,0,1,1]
sol.sortColors(nums)
print(nums)
nums = [2,1,0]
sol.sortColors(nums)
print(nums)
nums = [0,1,1]
sol.sortColors(nums)
print(nums)
nums = [0,0,0]
sol.sortColors(nums)
print(nums)
nums = [1,0]
sol.sortColors(nums)
print(nums)
nums = [0,2,0]
sol.sortColors(nums)
print(nums)