#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (33.01%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 42.8K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
# 
# 示例1:
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 
# 
# 示例2:
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 注意：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 25.44 % of python3 submissions
    Your memory usage beats 58.62 % of python3 submissions (13.2 MB)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if not s2 or len(s1) > len(s2):
            return False

        letters = {}
        for l in s1:
            letters[l] = letters.get(l,0)+1

        start, end = 0, 0
        while start < len(s2) and end < len(s2):
            while s2[start] not in letters and start==end and start < len(s2)-1:
                start += 1
                end += 1
            if not letters:
                return True
            if s2[end] in letters:
                if letters[s2[end]] > 1 :
                    letters[s2[end]] -= 1
                else:
                    del letters[s2[end]]
                end += 1
            else:
                if s2[start] in letters:
                    letters[s2[start]] += 1
                else:
                    letters[s2[start]] = 1
                start += 1

        if not letters:
            return True
        else:
            return False


        
# @lc code=end

sol = Solution()
print(sol.checkInclusion("adc","dcda"))
print(sol.checkInclusion("","dcda"))
print(sol.checkInclusion("adcke","ddueckcda"))
print(sol.checkInclusion("ab","eidboaoo"))