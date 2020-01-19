#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (63.52%)
# Likes:    370
# Dislikes: 0
# Total Accepted:    26.2K
# Total Submissions: 40.8K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    '''
    动态规划求解
    Your runtime beats 80.1 % of python3 submissions
    Your memory usage beats 59.06 % of python3 submissions (13.1 MB)
    '''
    def numTrees(self, n: int) -> int:
        cnt = [0 for i in range(n+1)]
        for i in range(n+1):
            if i <= 1:
                cnt[i] = 1
            else:
                for j in range(i):
                    cnt[i]+=cnt[j]*cnt[i-j-1]
        return cnt[n]
# @lc code=end

