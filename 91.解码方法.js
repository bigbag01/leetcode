/*
 * @lc app=leetcode.cn id=91 lang=javascript
 *
 * [91] 解码方法
 *
 * https://leetcode-cn.com/problems/decode-ways/description/
 *
 * algorithms
 * Medium (22.20%)
 * Likes:    273
 * Dislikes: 0
 * Total Accepted:    31K
 * Total Submissions: 134.5K
 * Testcase Example:  '"12"'
 *
 * 一条包含字母 A-Z 的消息通过以下方式进行了编码：
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * 
 * 给定一个只包含数字的非空字符串，请计算解码方法的总数。
 * 
 * 示例 1:
 * 
 * 输入: "12"
 * 输出: 2
 * 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
 * 
 * 
 * 示例 2:
 * 
 * 输入: "226"
 * 输出: 3
 * 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    var dp = new Array(s.length);
    if(s[0]=='0') return 0;
    if(s.length==1) return 1;
    
    if(s[s.length-1]=='0'&&s[s.length-2]!='1'&&s[s.length-2]!=2){
        return 0;
    }else{
        dp[s.length-1]=1;
    }
    for(let i=s.length-2;i>=0;i--){
        let tmp = parseInt(s.slice(i,i+2));
        if(s[i]!='0'){
            if(tmp==10||tmp==20||tmp>26||s[i+2]=='0'){
                dp[i]=dp[i+1]
            }else{
                dp[i]=dp[i+1]+(dp[i+2]||1)
            }
        }else{
            if(i-1<0||(s[i-1]!='1'&&s[i-1]!=2)) return 0
            dp[i]=dp[i+1]
        }
    };
    return dp[0];
};
// @lc code=end

console.log(numDecodings('12'))
console.log(numDecodings('226'))
console.log(numDecodings('112631018'))
console.log(numDecodings('0'))
console.log(numDecodings('00'))
console.log(numDecodings('100'))
console.log(numDecodings('301'))
console.log(numDecodings('110'))