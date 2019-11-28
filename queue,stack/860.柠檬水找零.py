#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
# Your runtime beats 59.28 % of python3 submissions
# Your memory usage beats 5.5 % of python3 submissions (14 MB)
#


# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 对于找零来说20没有意义，但是5和10都有，分别用两个计数器记录5和10的数量
        cnt_5=0
        cnt_10=0
        for b in bills:
            if b == 5:
                cnt_5+=1
            elif b == 10:
                if cnt_5 == 0:
                    return False
                else:
                    cnt_5-=1
                    cnt_10+=1
            elif b == 20:
                if cnt_10 > 0:
                    if cnt_5 == 0:
                        return False
                    else:
                        cnt_10-=1
                        cnt_5-=1
                else:
                    if cnt_5 >= 3:
                        cnt_5-=3
                    else:
                        return False
        return True
# @lc code=end

