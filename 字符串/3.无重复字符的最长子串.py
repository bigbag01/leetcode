#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.08%)
# Likes:    3099
# Dislikes: 0
# Total Accepted:    334.2K
# Total Submissions: 1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 89.16 % of python3 submissions
    Your memory usage beats 56.94 % of python3 submissions (13.3 MB)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        contains = {}
        i, start, max_len = 0, 0, 0
        while i < len(s):
            if s[i] in contains and contains[s[i]]>=start:
                start = contains[s[i]]+1
                contains[s[i]] = i
                i += 1
            else:
                contains[s[i]] = i
                i += 1
            if i - start > max_len:
                max_len = i - start              
        return max_len
# @lc code=end

sol = Solution()
sol.lengthOfLongestSubstring('abcabcbb')
