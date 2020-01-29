#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (45.96%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 25.6K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 注意数组中可能存在重复的元素。
# 
# 示例 1：
# 
# 输入: [1,3,5]
# 输出: 1
# 
# 示例 2：
# 
# 输入: [2,2,2,0,1]
# 输出: 0
# 
# 说明：
# 
# 
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
# 
# 
#

# @lc code=start
class Solution:


    '''
    二分递归查找
    192/192 cases passed (60 ms)
    Your runtime beats 73.15 % of python3 submissions
    Your memory usage beats 54.69 % of python3 submissions (13.5 MB)
    '''
    def findMin(self, rotateArray):
        if len(rotateArray) == 1:
            return rotateArray[0]
        if rotateArray[0] < rotateArray [-1]:
            return rotateArray[0]
        else:
            m = int(len(rotateArray)/2)
            l_min = self.findMin(rotateArray[:m])
            r_min = self.findMin(rotateArray[m:])
            return min(l_min,r_min)
# @lc code=end
sol = Solution()
print(sol.findMin([1,1])==1)
print(sol.findMin([1,1,3])==1)
print(sol.findMin([1,3,3])==1)
print(sol.findMin([0,0,0])==0)
print(sol.findMin([7,7,1,7])==1)
print(sol.findMin([3,1,3,3])==1)
print(sol.findMin([10,1,10,10,10])==1)
print(sol.findMin([7,7,1,1,7,7])==1)
print(sol.findMin([1])==1)
print(sol.findMin([2,2,2,0,1])==0)
