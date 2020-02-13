/*
 * @lc app=leetcode.cn id=5 lang=javascript
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (27.67%)
 * Likes:    1742
 * Dislikes: 0
 * Total Accepted:    179.9K
 * Total Submissions: 632.8K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 
 * 示例 1：
 * 
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入: "cbbd"
 * 输出: "bb"
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if(s.length==0) return s;
    var dp = new Array(s.length);
    var max = 0;
    var max_pos;
    for(var i=0;i<s.length;i++){
        dp[i] = new Array(s.length);
    }
    for(var i=0;i<s.length;i++){
        for(var j=0;j<s.length;j++){
            if(s[i]!=s[s.length-1-j]){
                dp[i][j]=0;
            }else{
                if(i==0||j==0)
                    dp[i][j]=1;
                else
                    dp[i][j]=dp[i-1][j-1]+1;
                if(dp[i][j]>max&&(Math.abs(s.length-j-1-i)+1==dp[i][j])){
                    max = dp[i][j];
                    max_pos = [i,j];
                }
            }
        }
    };
    
    if(max==1)
        return s[max_pos[0]];
    return s.slice(max_pos[0]+1-max,max_pos[0]+1)
};
// @lc code=end


console.log(longestPalindrome('abba'))
console.log(longestPalindrome('abccda'))
console.log(longestPalindrome('abcd'))
console.log(longestPalindrome('a'))
console.log(longestPalindrome("aacdefcaa"))
debugger