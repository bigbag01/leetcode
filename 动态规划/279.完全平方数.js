/*
 * @lc app=leetcode.cn id=279 lang=javascript
 *
 * [279] 完全平方数
 *
 * https://leetcode-cn.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (51.33%)
 * Likes:    302
 * Dislikes: 0
 * Total Accepted:    35.9K
 * Total Submissions: 67.1K
 * Testcase Example:  '12'
 *
 * 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
 * 
 * 示例 1:
 * 
 * 输入: n = 12
 * 输出: 3 
 * 解释: 12 = 4 + 4 + 4.
 * 
 * 示例 2:
 * 
 * 输入: n = 13
 * 输出: 2
 * 解释: 13 = 4 + 9.
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    
    var dp = new Array(n+1);
    for(let i=1;i<=n;i++){
        var max_root = Math.floor(Math.sqrt(i));
        var close_square = max_root*max_root;
        
        if(max_root==1)
            dp[i] = i;
        else{
            if(i==close_square){
                dp[i]=1
            }else{
                dp[i] = dp[close_square]+dp[i-close_square];
                for(let j=max_root-1;j>max_root/2;j--){
                    dp[i] = Math.min(dp[i],dp[j*j]+dp[i-j*j])
                }
                
            }
        }
    }
    return dp[n]
};
// @lc code=end

console.log(numSquares(12))
console.log(numSquares(32))
console.log(numSquares(48))