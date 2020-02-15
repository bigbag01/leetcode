/*
 * @lc app=leetcode.cn id=300 lang=javascript
 *
 * [300] 最长上升子序列
 *
 * https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (43.37%)
 * Likes:    417
 * Dislikes: 0
 * Total Accepted:    47.6K
 * Total Submissions: 108.3K
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 给定一个无序的整数数组，找到其中最长上升子序列的长度。
 * 
 * 示例:
 * 
 * 输入: [10,9,2,5,3,7,101,18]
 * 输出: 4 
 * 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
 * 
 * 说明:
 * 
 * 
 * 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
 * 你算法的时间复杂度应该为 O(n^2) 。
 * 
 * 
 * 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if(nums.length==0) return 0;
    var dp=new Array(nums.length);
    for(let i=0;i<nums.length;i++){
        let j=i-1;
        let small=0;
        for(let j=i-1;j>=0;j--){
            if(nums[j]<nums[i])
                if(dp[j]>small)
                    small=dp[j];
        }
        dp[i] = small+1;
    }
    return Math.max(...dp);
};
// @lc code=end

console.log(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
console.log(lengthOfLIS([1,2,3]))
console.log(lengthOfLIS([]))
console.log(lengthOfLIS([6,5,1]))