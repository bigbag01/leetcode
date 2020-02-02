#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (48.09%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 31.2K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 96.39 % of python3 submissions
    Your memory usage beats 49.79 % of python3 submissions (13.1 MB)
    '''
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            raise ValueError
        if n <= 6:
            return n
        table = [0 for i in range(n+1)]
        table[1] = 1
        t2,t3,t5 = 1,1,1
        for i in range(2,n+1):
            multp2 = table[t2]*2
            multp3 = table[t3]*3
            multp5 = table[t5]*5
            current = min(multp2,multp3,multp5)
            table[i] = current
            if multp5 <= current:
                t5 += 1
            if multp3 <= current:
                t3 += 1
            if multp2 <= current:
                t2 += 1
        
        return table[n]
# @lc code=end

