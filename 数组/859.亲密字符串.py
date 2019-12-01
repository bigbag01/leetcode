#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
# Your runtime beats 90.13 % of python3 submissions
# Your memory usage beats 5.79 % of python3 submissions (14.1 MB)
# 

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # 先判断二者长度是否相等，不相等直接false
        if len(A)!=len(B):
            return False
        diff1=[]
        diff2=[]
        appear={}
        repeat=False
        for i in range(len(A)):
            # 记录同样位置的不同字符对
            if A[i]!=B[i]:
                if len(diff1)==0:
                    diff1=[A[i],B[i]]
                elif len(diff2)==0:
                    diff2=[A[i],B[i]]
                else:
                    # 如果不同字符对出现2次以上就false
                    return False
            # 对于字符对相同，记录是否有重复出现
            else:
                if A[i] in appear:
                    repeat=True
                else:
                    appear[A[i]]=1
        # 如果只有一个不同字符对，就false
        if len(diff1)>0 and len(diff2)==0:
            return False
        # 如果有两个不同字符对，比较是否交换后相同
        if len(diff1)>0 and len(diff2)>0:
            return (diff1[0]==diff2[1]) and (diff1[1]==diff2[0])
        # 如果两个字符串相等，查找是否有重复出现
        if len(diff1)==0 and len(diff2)==0:
            return repeat
        
# @lc code=end

