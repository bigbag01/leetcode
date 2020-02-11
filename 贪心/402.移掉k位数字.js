/*
 * @lc app=leetcode.cn id=402 lang=javascript
 *
 * [402] 移掉K位数字
 *
 * https://leetcode-cn.com/problems/remove-k-digits/description/
 *
 * algorithms
 * Medium (26.68%)
 * Likes:    151
 * Dislikes: 0
 * Total Accepted:    10.4K
 * Total Submissions: 37.4K
 * Testcase Example:  '"1432219"\n3'
 *
 * 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
 * 
 * 注意:
 * 
 * 
 * num 的长度小于 10002 且 ≥ k。
 * num 不会包含任何前导零。
 * 
 * 
 * 示例 1 :
 * 
 * 
 * 输入: num = "1432219", k = 3
 * 输出: "1219"
 * 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
 * 
 * 
 * 示例 2 :
 * 
 * 
 * 输入: num = "10200", k = 1
 * 输出: "200"
 * 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
 * 
 * 
 * 示例 3 :
 * 
 * 
 * 输入: num = "10", k = 2
 * 输出: "0"
 * 解释: 从原数字移除所有的数字，剩余为空就是0。
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    if(num.length==0) return 0;
    if(num==0) return num;
    var stack=[0,num[0]];
    num=num.slice(1);
    var cur,nxt;
    while(k>0){
        //console.log(stack)
        cur = stack.pop();
        nxt = num[0]||'0';
        if(cur>=stack[stack.length-1]&&cur>nxt||num.length<=k-1){
            k--;
        }else{
            stack.push(cur)
            stack.push(nxt);
            num=num.slice(1);
        }
    }
    if(k==0){
        num = stack.join('')+num;
        let i=0;
        while(num[i]==0&&i<num.length-1){
            i++;
        }
        num = num.slice(i);
    }

    return num
};
console.log(removeKdigits("1432219",3))
console.log(removeKdigits("10200",1))
console.log(removeKdigits("10",2))
console.log(removeKdigits("151321",2))
// @lc code=end

