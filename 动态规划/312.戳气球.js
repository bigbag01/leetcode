/*
 * @lc app=leetcode.cn id=312 lang=javascript
 *
 * [312] 戳气球
 *
 * https://leetcode-cn.com/problems/burst-balloons/description/
 *
 * algorithms
 * Hard (56.32%)
 * Likes:    194
 * Dislikes: 0
 * Total Accepted:    7.2K
 * Total Submissions: 12.5K
 * Testcase Example:  '[3,1,5,8]'
 *
 * 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
 * 
 * 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
 * left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
 * 
 * 求所能获得硬币的最大数量。
 * 
 * 说明:
 * 
 * 
 * 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
 * 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
 * 
 * 
 * 示例:
 * 
 * 输入: [3,1,5,8]
 * 输出: 167 
 * 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
 * coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function(nums) {
    var cache = new Array(nums.length+1);
    for(let i=0;i<=nums.length;i++){
        cache[i]=new Array(nums.length+1);
    }
    function helper(start,end,head,tail){
        if(start==end){
            cache[start][end]=0
            return 0;
        }
        else{
            if(cache[start][end]!=undefined){
                return cache[start][end]
            }
            else{
                var max = 0;
                for(let i=start;i<end;i++){
                    let cur = nums[i]*head*tail+helper(start,i,head,nums[i])+helper(i+1,end,nums[i],tail);
                    max = Math.max(max,cur);
                }
                cache[start][end]=max;
                return max;
            }
            
        }
    }
    return helper(0,nums.length,1,1)
};
// @lc code=end
console.log(maxCoins([3,1,5,8]))
console.log(maxCoins([3,2,4,1,5]))
console.log(maxCoins([1,2,3,4,5]))
console.log(maxCoins([]))
