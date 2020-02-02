#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (41.65%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    58K
# Total Submissions: 135.2K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 案例:
# 
# 
# s = "leetcode"
# 返回 0.
# 
# s = "loveleetcode",
# 返回 2.
# 
# 
# 
# 
# 注意事项：您可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 解1
        '''
        Your runtime beats 49.36 % of python3 submissions
        Your memory usage beats 54.14 % of python3 submissions (13.3 MB)
        '''
        counter = {}
        for l in s:
            counter[l] = counter.get(l,0)+1
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1   
             

        # 解2 只包含小写字母可以用大小为26的数组
        '''
        Your runtime beats 30.07 % of python3 submissions
        Your memory usage beats 54.44 % of python3 submissions (13.1 MB)
        
        counter = [0 for i in range(26)]
        for l in s:
            counter[ord(l)-97]+=1
        for i in range(len(s)):
            if counter[ord(s[i])-97]==1:
                return i
        return -1
        '''
        

        #解3 利用python字符串的count函数
        '''
        对于很长的testcase会超时……

        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1
        '''

# @lc code=end

