#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (47.03%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    42.9K
# Total Submissions: 90.6K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 22.57 % of python3 submissions
    Your memory usage beats 54.44 % of python3 submissions (13.2 MB)
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n&(n-1)
    '''

    '''
    Your runtime beats 69.79 % of python3 submissions
    Your memory usage beats 54.44 % of python3 submissions (13 MB)
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n&(n-1)==0
# @lc code=end

sol = Solution()
print(sol.isPowerOfTwo(0))
print(sol.isPowerOfTwo(1))
print(sol.isPowerOfTwo(2))
print(sol.isPowerOfTwo(3))
print(sol.isPowerOfTwo(4))
print(sol.isPowerOfTwo(5))