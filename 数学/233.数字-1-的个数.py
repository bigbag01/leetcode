#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (31.37%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 14.4K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 示例:
# 
# 输入: 13
# 输出: 6 
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        Your runtime beats 52.27 % of python3 submissions
        Your memory usage beats 55.55 % of python3 submissions (13.1 MB)
        '''
        if n <= 0:
            return 0
        if n < 10:
            return 1
        import math
        digits = int(math.log10(n))
        tens = 10**digits
        first_digit = int(n/tens)
        if first_digit == 1:
            return (n-tens+1)\
        + self.countDigitOne(tens-1)\
        + self.countDigitOne(n-first_digit*tens)
        else:
            return tens\
        +first_digit*self.countDigitOne(tens-1)\
        + self.countDigitOne(n-first_digit*tens)        
# @lc code=end

