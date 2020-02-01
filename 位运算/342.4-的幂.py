#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (46.95%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 37.4K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
# 
# 示例 1:
# 
# 输入: 16
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 5
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 7.63 % of python3 submissions
    Your memory usage beats 49.07 % of python3 submissions (13 MB)
    
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        # 不是2的幂，一定不是4的幂
        if num & (num-1) != 0:
            return False
        # 校验奇数位
        return (num & 0x55555555) != 0 
    '''

    '''
    Your runtime beats 92.54 % of python3 submissions
    Your memory usage beats 49.07 % of python3 submissions (13.1 MB)
    '''
    def isPowerOfFour(self, num: int) -> bool:
        # 校验是否为2的幂
        if num <= 0 or num & (num-1) != 0:
            return False
        # 校验奇数位
        return num % 3 == 1 
    
# @lc code=end

sol = Solution()
print(sol.isPowerOfFour(1))
print(sol.isPowerOfFour(2))
print(sol.isPowerOfFour(3))
print(sol.isPowerOfFour(4))
print(sol.isPowerOfFour(8))