/*
 * @lc app=leetcode.cn id=44 lang=javascript
 *
 * [44] 通配符匹配
 *
 * https://leetcode-cn.com/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (25.38%)
 * Likes:    261
 * Dislikes: 0
 * Total Accepted:    17.6K
 * Total Submissions: 67.6K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
 * 
 * '?' 可以匹配任何单个字符。
 * '*' 可以匹配任意字符串（包括空字符串）。
 * 
 * 
 * 两个字符串完全匹配才算匹配成功。
 * 
 * 说明:
 * 
 * 
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 * 
 * 示例 2:
 * 
 * 输入:
 * s = "aa"
 * p = "*"
 * 输出: true
 * 解释: '*' 可以匹配任意字符串。
 * 
 * 
 * 示例 3:
 * 
 * 输入:
 * s = "cb"
 * p = "?a"
 * 输出: false
 * 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
 * 
 * 
 * 示例 4:
 * 
 * 输入:
 * s = "adceb"
 * p = "*a*b"
 * 输出: true
 * 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
 * 
 * 
 * 示例 5:
 * 
 * 输入:
 * s = "acdcb"
 * p = "a*c?b"
 * 输入: false
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
// 思路1是用DP
var isMatch = function(s, p) {
    var dp = new Array(s.length+1);
    for(let i=0;i<dp.length;i++){
        dp[i]=new Array(p.length+1)
        dp[i].fill(false)
    }
    dp[0][0]=true;
    for (let j=1;j<=p.length;j++){
        dp[0][j] = dp[0][j-1]&&p[j-1]=='*'
    }
    for (let i=1;i<=s.length;i++){
        dp[i][0] = false
    }
    s = ' '+s;
    p = ' '+p
    for(var i=1;i<s.length;i++){
        for(var j=1;j<p.length;j++){
            if(s[i]==p[j]||p[j]=='?')
                dp[i][j]=dp[i-1][j-1]
            else if(p[j]=='*')
                dp[i][j]=dp[i][j-1]||dp[i-1][j]
            else
                dp[i][j]=false
        }
    }
    return dp[s.length-1][p.length-1]
};

// 思路2
// 用正则做一下,会发生time limit exceeded
// var isMatch = function(s, p){
//     var pattStr = p.replace(/\?/g,'[a-z]').replace(/\*/g,'[a-z]*')
//     var patt = new RegExp('^'+pattStr+'$');
//     return patt.test(s)
// } 

// 思路3 back-tracing
// time limit exceeded
// var isMatch = function(s,p){
//     var checkFlag = check(s,p);
//     if(checkFlag!=undefined) return checkFlag
//     var trimed = trim(s,p);
//     if(trimed.length==0) return false
//     s = trimed[0];
//     p = trimed[1];
//     checkFlag = check(s,p);
//     if(checkFlag!=undefined) return checkFlag
    
//     for(let i=0;i<s.length;i++){
//         if(isMatch(s.slice(i),p.slice(1)))
//             return true
//     }
//     return false

//     //return isMatch(s,p)

// }
// function check(s,p){
//     if(p=='') return s==''
//     if(!(/[^\*]/.test(p))) return true
//     if (s=='') return false
// }
// function trim(s,p){
//     var si=0,pi=0,sj=s.length-1,pj=p.length-1;
//     while(si<s.length && pi<p.length && p[pi]!='*' ){
//         if(s[si]==p[pi]||p[pi]=='?'){
//             si++;
//             pi++;
//         }else{
//             return []
//         }
//     }
//     s = s.slice(si)
//     p = p.slice(pi)
//     while(sj>=0&&pj>=0&&p[pj]!='*'){
//         if(s[sj]==p[pj]||p[pj]=='?'){
//             sj--;pj--;
//         } 
//         else
//             return []
//     }
//     s = s.slice(0,sj+1)
//     p = p.slice(0,pj+1)
//     return [s,p]
// }

// @lc code=end

console.log(isMatch('aa','a'))
console.log(isMatch("aa",'*'))
console.log(isMatch('cb','?a'))
console.log(isMatch('adceb','*a*b'))
console.log(isMatch('acdcb','?a*c?b'))
console.log(isMatch("mississippi","m??*ss*?i*pi"))