#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#
# https://leetcode-cn.com/problems/super-pow/description/
#
# algorithms
# Medium (36.92%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 6.8K
# Testcase Example:  '2\n[3]'
#
# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
# 
# 示例 1:
# 
# 输入: a = 2, b = [3]
# 输出: 8
# 
# 
# 示例 2:
# 
# 输入: a = 2, b = [1,0]
# 输出: 1024
# 
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # (x * y) % k = (x%k)*(y%k)%k
        if not b:
            return 1
        last = b.pop()
        return (self.superPow(a,b)**10 %1337) * (a**last % 1337 ) % 1337


# @lc code=end

