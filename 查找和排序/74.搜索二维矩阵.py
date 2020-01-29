#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (36.42%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 76.8K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 示例 1:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 
#

# @lc code=start
class Solution:
    '''
    136/136 cases passed (76 ms)
    Your runtime beats 74.61 % of python3 submissions
    Your memory usage beats 55.77 % of python3 submissions (15 MB)
    '''
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left,right,top,bottom = 0,n-1,0,m-1
        while left <= right and top <= bottom :
            i,j = int((top+bottom)/2),int((left+right)/2)
            if matrix[i][j] == target:  # hit
                return True
            elif matrix[i][j] < target: # 当前数小于目标
                if matrix[i][right] == target:  # 当前行区域最大值hit
                    return True
                elif matrix[i][right] > target: # 当前行区域最大值大于目标
                    left = j + 1
                else:
                    top = i + 1
            else:
                if matrix[i][left] == target: #hit
                    return True
                elif matrix[i][left] < target:
                    right = j - 1
                else:
                    bottom = i - 1
        return False





# @lc code=end

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],20))
print(sol.searchMatrix([[0,1],[2,3]],1))
print(sol.searchMatrix([],1))
