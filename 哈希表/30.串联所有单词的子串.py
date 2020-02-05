#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (28.02%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 75.1K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
# 
# 示例 2：
# 
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
# 
# 
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 44.63 % of python3 submissions
    Your memory usage beats 55.24 % of python3 submissions (13.2 MB)
    '''
    def findSubstring(self, s: str, words) :
        if not s or not words:
            return []
        width = len(words[0])
        if len(s) < len(words)*width:
            return []
        hashmap = {}
        results = []
        total_len = width*len(words)
        for word in words:
            hashmap[word] = hashmap.get(word,0)+1
        for i in range(0,len(s)-total_len+1):
            current = s[i:i+total_len]
            flag = True
            cur_map = {}
            segs = [current[j:j+width] for j in range(0,total_len,width)]
            #print(segs)
            for seg in segs:
                cur_map[seg] = cur_map.get(seg,0)+1
                if seg not in hashmap or cur_map[seg]>hashmap[seg]:
                    #print(seg,cur_map)
                    flag = False
                    break
            if flag:
                results.append(i)
        return results

            
# @lc code=end

sol = Solution()
print(sol.findSubstring("abaababbaba",["ab","ba","ab","ba"]))