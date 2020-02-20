/*
 * @lc app=leetcode.cn id=474 lang=javascript
 *
 * [474] 一和零
 *
 * https://leetcode-cn.com/problems/ones-and-zeroes/description/
 *
 * algorithms
 * Medium (47.44%)
 * Likes:    117
 * Dislikes: 0
 * Total Accepted:    5.5K
 * Total Submissions: 11.1K
 * Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
 *
 * 在计算机界中，我们总是追求用有限的资源获取最大的收益。
 * 
 * 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
 * 
 * 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
 * 
 * 注意:
 * 
 * 
 * 给定 0 和 1 的数量都不会超过 100。
 * 给定字符串数组的长度不会超过 600。
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
 * 输出: 4
 * 
 * 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: Array = {"10", "0", "1"}, m = 1, n = 1
 * 输出: 2
 * 
 * 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
 * 
 * 
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    counter={};
    for(let str of strs){
        counter[str] = str.split('').reduce((cnt,cur)=>{
            ++cnt[cur];return cnt;
        },[0,0])
    }

    var dp = new Array(m+1);
    for(let i=0;i<m+1;i++){
        dp[i] = new Array(n+1);
        dp[i].fill(0);
    }
    for(let str of strs){
        cnt = counter[str];
        for(let i=m;i>=cnt[0];i--){
            for(let j=n;j>=cnt[1];j--){
                dp[i][j] = Math.max(dp[i][j],1+dp[i-cnt[0]][j-cnt[1]])
            }
        }
    }
    return dp[m][n];
};
// @lc code=end

console.log(findMaxForm(["10", "0001", "111001", "1", "0"],5,3))
console.log(findMaxForm(['10','0','1'],1,1))
console.log(findMaxForm([],1,1))
console.log(findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"],9,80))