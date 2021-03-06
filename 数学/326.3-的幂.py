#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (45.42%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 74.5K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 
# 示例 1:
# 
# 输入: 27
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 0
# 输出: false
# 
# 示例 3:
# 
# 输入: 9
# 输出: true
# 
# 示例 4:
# 
# 输入: 45
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # max_exp = int(math.log(2**31-1,3)) = 19
        # 3**19 = 1162261467
        return n > 0 and 1162261467 % n == 0 
# @lc code=end

