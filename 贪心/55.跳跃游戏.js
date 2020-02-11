/*
 * @lc app=leetcode.cn id=55 lang=javascript
 *
 * [55] 跳跃游戏
 *
 * https://leetcode-cn.com/problems/jump-game/description/
 *
 * algorithms
 * Medium (37.00%)
 * Likes:    454
 * Dislikes: 0
 * Total Accepted:    57.6K
 * Total Submissions: 152.1K
 * Testcase Example:  '[2,3,1,1,4]'
 *
 * 给定一个非负整数数组，你最初位于数组的第一个位置。
 * 
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * 
 * 判断你是否能够到达最后一个位置。
 * 
 * 示例 1:
 * 
 * 输入: [2,3,1,1,4]
 * 输出: true
 * 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,2,1,0,4]
 * 输出: false
 * 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
/* Your runtime beats 88.51 % of javascript submissions
Your memory usage beats 84.16 % of javascript submissions (35.6 MB) */
var canJump = function(nums) {
    var len = nums.length;
    if (len<=1) return true;
    var last=0;
    for(let i=0;i<len;i++){
        var step=nums[i];
        if(last<i) return false;
        last = Math.max(i+step,last);
        if(last>=len-1) return true;
    }
    return last>=len-1
};
// @lc code=end

console.log(canJump([3,2,1,1,4]))