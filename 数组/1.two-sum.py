#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = nums.copy()
        snums.sort()
        i = 0
        j = len(snums)-1
        while i<j:
            cur_sum = snums[i]+snums[j]
            if cur_sum == target:
                i1 = nums.index(snums[i])
                i2 = nums.index(snums[j])
                if i1==i2:
                    nums[i1]=None
                    i2 = nums.index(snums[j])
                return [i1,i2]
            elif cur_sum < target:
                i+=1
            else:
                j-=1
        
# @lc code=end

