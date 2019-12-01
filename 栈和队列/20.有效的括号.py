#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        stack = []
        match={')':'(',']':'[','}':'{'}
        for l in s:
            if l in ['(','[','{']:
                stack.append(l)
            else:
                try:
                    pre = stack.pop()
                    if match[l] != pre:
                        return False
                except:
                    return False

        return not stack
                
# @lc code=end

