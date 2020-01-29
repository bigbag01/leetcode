#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.31%)
# Likes:    2065
# Dislikes: 0
# Total Accepted:    135K
# Total Submissions: 368.8K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    '''
    解法1，合并两个数组，然后找中位数，时间复杂度是O(m+n)，不符合题目要求，不写了
    '''

    '''
    解法2，找到划分点，使得两侧数一样多
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            return self.findMedian(nums2)
        elif not nums2:
            return self.findMedian(nums1)
        elif nums1[0]>nums2[-1]:
            return self.findMedian(nums2+nums1)
        elif nums2[0]>nums1[-1]:
            return self.findMedian(nums1+nums2)
        else:
            m = len(nums1)
            n = len(nums2)
            if m > n:
                nums1,nums2,m,n = nums2,nums1,n,m
            l,r,half = 0,m,int((m+n+1)/2)
            while l<=r:
                i = int((l+r)/2)
                j = half - i
                if i < m and nums1[i] <nums2[j-1]:
                    l = i + 1
                elif i > 0 and nums1[i-1] > nums2[j]:
                    r = i - 1
                else:
                    #print(i,j)
                    if i == 0:
                        left_max = nums2[j-1]
                    elif j == 0:
                        left_max = nums1[i-1]
                    else:
                        left_max = max(nums1[i-1],nums2[j-1])
                    
                    if (m+n)%2:
                        return left_max

                    if i == m:
                        right_min = nums2[j]
                    elif j == n:
                        right_min = nums1[i]
                    else:
                        right_min = min(nums1[i],nums2[j])

                    return (left_max+right_min)/2
                    


    def findMedian(self,nums):
        if len(nums)%2 :
            return nums[int(len(nums)/2)]
        else:
            return (nums[int(len(nums)/2)]+nums[int(len(nums)/2)-1])/2
# @lc code=end

sol = Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))
print(sol.findMedianSortedArrays([1,3],[2]))
print(sol.findMedianSortedArrays([1,2,3,9],[6,7,8]))
print(sol.findMedianSortedArrays([1],[4]))
print(sol.findMedianSortedArrays([],[3,4]))
print(sol.findMedianSortedArrays([5,8,10,33],[1,44]))