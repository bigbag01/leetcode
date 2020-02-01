#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (64.84%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 29.1K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,3,2]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 参考题解,用a，b分别记录出现2次和出现1次的位
        a,b = 0,0
        for n in nums:
            # ab 00->01->10->00
            b = b^n & ~a 
            a = a^n & ~b  
        return b

# @lc code=end

