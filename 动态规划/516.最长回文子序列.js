/*
 * @lc app=leetcode.cn id=516 lang=javascript
 *
 * [516] 最长回文子序列
 *
 * https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
 *
 * algorithms
 * Medium (47.39%)
 * Likes:    147
 * Dislikes: 0
 * Total Accepted:    12.1K
 * Total Submissions: 24K
 * Testcase Example:  '"bbbab"'
 *
 * 给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
 * 
 * 示例 1:
 * 输入:
 * 
 * 
 * "bbbab"
 * 
 * 
 * 输出:
 * 
 * 
 * 4
 * 
 * 
 * 一个可能的最长回文子序列为 "bbbb"。
 * 
 * 示例 2:
 * 输入:
 * 
 * 
 * "cbbd"
 * 
 * 
 * 输出:
 * 
 * 
 * 2
 * 
 * 
 * 一个可能的最长回文子序列为 "bb"。
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    if(s.length==0) return 0
    var r = s.split('').reverse().join('');
    var n = s.length;
    var dp = new Array(n);
    for(var i=0;i<n;i++){
        dp[i] = new Array(n);
    }
    dp[0][0]=(s[0]==r[0]?1:0);
    for(var i=1;i<n;i++){
        dp[i][0] = (s[i]!=r[0]&&dp[i-1][0]==0)?0:1;
    }
    for(var j=1;j<n;j++){
        dp[0][j] = (s[0]!=r[j]&&dp[0][j-1]==0)?0:1;
    }
    for(var i=1;i<n;i++){
        for(var j=1;j<n;j++){
            if(s[i]==r[j])
                dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
            else{
                dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1])
            }
        }
    }
    return dp[n-1][n-1];
};
// @lc code=end

console.log(longestPalindromeSubseq('bbbab'))
console.log(longestPalindromeSubseq(''))
console.log(longestPalindromeSubseq('cbbd'))
console.log(longestPalindromeSubseq('a'))