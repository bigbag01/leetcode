/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 *
 * https://leetcode-cn.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (56.68%)
 * Likes:    926
 * Dislikes: 0
 * Total Accepted:    243.5K
 * Total Submissions: 426.9K
 * Testcase Example:  '121'
 *
 * 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
 * 
 * 示例 1:
 * 
 * 输入: 121
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: -121
 * 输出: false
 * 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
 * 
 * 
 * 示例 3:
 * 
 * 输入: 10
 * 输出: false
 * 解释: 从右向左读, 为 01 。因此它不是一个回文数。
 * 
 * 
 * 进阶:
 * 
 * 你能不将整数转为字符串来解决这个问题吗？
 * 
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    /* 11509/11509 cases passed (212 ms)
    Your runtime beats 83.71 % of javascript submissions
    Your memory usage beats 85.94 % of javascript submissions (44.9 MB) */
    if(x<0){
        return false
    }
    var power = Math.floor(Math.log10(x));
    while(power>=0){
        var hi = Math.floor(x/(10**power));
        var lo = Math.floor(x%10);
        if (hi!=lo){
            return false;
        }else{
            x = x - hi*(10**power);
            x = (x-lo)/10;
            power -=2;
        }
    }
    return true;
};
// @lc code=end

// console.log(isPalindrome(11))
// console.log(isPalindrome(0))
// console.log(isPalindrome(-1))
// console.log(isPalindrome(121))
// console.log(isPalindrome(10))