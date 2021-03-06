/*
 * @lc app=leetcode.cn id=738 lang=javascript
 *
 * [738] 单调递增的数字
 *
 * https://leetcode-cn.com/problems/monotone-increasing-digits/description/
 *
 * algorithms
 * Medium (39.84%)
 * Likes:    39
 * Dislikes: 0
 * Total Accepted:    3.1K
 * Total Submissions: 7.4K
 * Testcase Example:  '10'
 *
 * 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
 * 
 * （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
 * 
 * 示例 1:
 * 
 * 输入: N = 10
 * 输出: 9
 * 
 * 
 * 示例 2:
 * 
 * 输入: N = 1234
 * 输出: 1234
 * 
 * 
 * 示例 3:
 * 
 * 输入: N = 332
 * 输出: 299
 * 
 * 
 * 说明: N 是在 [0, 10^9] 范围内的一个整数。
 * 
 */

// @lc code=start
/**
 * @param {number} N
 * @return {number}
 */
var monotoneIncreasingDigits = function(N) {
    var digits = String(N).split('').map(Number);
    var i=0;
    while(i<digits.length-1&&digits[i]<=digits[i+1]){
        i++;
    }
    if(i==digits.length-1&&digits[i-1]<=digits[i]){
        return N
    }
    var peak = digits[i];
    var k=0;
    while(digits[k]!=peak) k++;
    digits[k]=(peak+9)%10;
    
    for(i=k+1;i<digits.length;i++){
        digits[i]=9;
    }
    return digits.reduce((total,cur,i)=>{
        return total+cur*(10**(digits.length-i-1));
    },0)
};
// @lc code=end

console.log(monotoneIncreasingDigits(10))
console.log(monotoneIncreasingDigits(1234))
console.log(monotoneIncreasingDigits(332))
console.log(monotoneIncreasingDigits(997))
console.log(monotoneIncreasingDigits(1001))