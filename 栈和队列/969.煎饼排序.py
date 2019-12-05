#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions 

# @lc code=start
class Solution:
    def pancakeSort(self, A) :
        ks = []
        i = len(A)-1
        while i > 0:
            cur_max = max(A[:i+1])
            if A[i] == cur_max:
                i -= 1
                continue
            max_index = A[:i+1].index(cur_max)
            if max_index!=0:
                ks.append(max_index+1)
                A[:max_index+1]=self.reverse(A[:max_index+1])
            ks.append(i+1)
            A[:i+1] = self.reverse(A[:i+1])
        return ks


    def reverse(self,ll):
        ll.reverse()
        return ll
# @lc code=end

ss=Solution()
print(ss.pancakeSort([3,2,4,1]))