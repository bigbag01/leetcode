/*
 * @lc app=leetcode.cn id=213 lang=javascript
 *
 * [213] 打家劫舍 II
 *
 * https://leetcode-cn.com/problems/house-robber-ii/description/
 *
 * algorithms
 * Medium (35.34%)
 * Likes:    179
 * Dislikes: 0
 * Total Accepted:    19.6K
 * Total Submissions: 54.1K
 * Testcase Example:  '[2,3,2]'
 *
 * 
 * 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
 * 
 * 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
 * 
 * 示例 1:
 * 
 * 输入: [2,3,2]
 * 输出: 3
 * 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1,2,3,1]
 * 输出: 4
 * 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
 * 偷窃到的最高金额 = 1 + 3 = 4 。
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length==0) return 0;
    if(nums.length<3){
        return Math.max(...nums);
    }
    return Math.max(rob_line(nums.slice(1)),rob_line(nums.slice(0,-1)))
};

var rob_line = function(nums) {
    // income[i]表示从0-i，选中i时的最大收入
    if(nums.length==0) return 0;
    if(nums.length<3){
        return Math.max(...nums);
    };
    var income = new Array(nums.length);
    income[0] = nums[0];
    income[1] = Math.max(income[0],nums[1]);
    income[2] = nums[0]+nums[2];
    for(let i=3;i<nums.length;i++){
        income[i] = nums[i]+Math.max(income[i-2],income[i-3]);
    }
    return Math.max(income[nums.length-1],income[nums.length-2])

};

// @lc code=end

console.log(rob([2,3,2]))
console.log(rob([1,2,3,1]))
console.log(rob([2,7,9,3,1]))