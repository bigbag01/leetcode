#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (37.86%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    37.9K
# Total Submissions: 98.6K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target = 5，返回 true。
# 
# 给定 target = 20，返回 false。
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        129/129 cases passed (48 ms)
        Your runtime beats 47.16 % of python3 submissions
        Your memory usage beats 53.8 % of python3 submissions (18.3 MB)
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        def searchRegion(left,right,top,bottom):
            if left > n-1 or right < 0 or top > m-1 or bottom < 0 or left > right or top > bottom:
                return False
            center_h = int((top+bottom)/2)
            center_w = int((left+right)/2)
            center = matrix[center_h][center_w]
            if center == target:
                return True
            elif center < target:
                return searchRegion(center_w+1,right,top,bottom) or searchRegion(left,right,center_h+1,bottom)
            else :
                return searchRegion(left,center_w-1,top,bottom) or searchRegion(left,right,top,center_h-1)

        return searchRegion(0,n-1,0,m-1)
        
# @lc code=end

sol = Solution()
print(sol.searchMatrix([[0]],0))