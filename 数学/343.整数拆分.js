/*
 * @lc app=leetcode.cn id=343 lang=javascript
 *
 * [343] 整数拆分
 *
 * https://leetcode-cn.com/problems/integer-break/description/
 *
 * algorithms
 * Medium (53.12%)
 * Likes:    157
 * Dislikes: 0
 * Total Accepted:    16.1K
 * Total Submissions: 29.8K
 * Testcase Example:  '2'
 *
 * 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
 * 
 * 示例 1:
 * 
 * 输入: 2
 * 输出: 1
 * 解释: 2 = 1 + 1, 1 × 1 = 1。
 * 
 * 示例 2:
 * 
 * 输入: 10
 * 输出: 36
 * 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
 * 
 * 说明: 你可以假设 n 不小于 2 且不大于 58。
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
    /* Your runtime beats 78.23 % of javascript submissions
    Your memory usage beats 73.79 % of javascript submissions (33.8 MB) */
    if(n<=3) return n-1;
    if(n==4) return 4;
    switch(n%3){
        case 0:
            return 3**(n/3)
        case 1:
            return 4*(3**((n-4)/3))
        case 2:
            return 2*(3**((n-2)/3))
    }
    
};
// @lc code=end

console.log(integerBreak(2))
console.log(integerBreak(10))