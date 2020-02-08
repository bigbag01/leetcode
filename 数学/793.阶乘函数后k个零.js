/*
 * @lc app=leetcode.cn id=793 lang=javascript
 *
 * [793] 阶乘函数后K个零
 *
 * https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/description/
 *
 * algorithms
 * Hard (31.62%)
 * Likes:    32
 * Dislikes: 0
 * Total Accepted:    1.1K
 * Total Submissions: 3.3K
 * Testcase Example:  '0'
 *
 *  f(x) 是 x! 末尾是0的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且0! = 1）
 * 
 * 例如， f(3) = 0 ，因为3! = 6的末尾没有0；而 f(11) = 2 ，因为11!= 39916800末端有2个0。给定
 * K，找出多少个非负整数x ，有 f(x) = K 的性质。
 * 
 * 
 * 示例 1:
 * 输入:K = 0
 * 输出:5
 * 解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。
 * 
 * 示例 2:
 * 输入:K = 5
 * 输出:0
 * 解释:没有匹配到这样的 x!，符合K = 5 的条件。
 * 
 * 
 * 注意：
 * 
 * 
 * 
 * K是范围在 [0, 10^9] 的整数。
 * 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} K
 * @return {number}
 */
var preimageSizeFZF = function(K) {
    // 出现一个5一个2就会得到末尾一个0，除了5的幂的情况，10的幂的情况，其他每5个数多一个0
    // 返回结果一定是0或者5
    // K =      x/5+x/25+x/125+...+x/5^(t-1)+x/5^t (t>=1)
    // 5K = x + x/5+x/25+x/125+...x/5^(t-1)
    // 4K = x-x/5^t

    if (K==0){
        return 5
    }else{
        for(let x=Math.ceil(4*K/5)*5;x<=5*K;x+=5){
            if(f(x)==K){
                console.log(`x=${x}`)
                return 5
            }else if (f(x)>K){
                return 0
            }
        }
        return 0
    }
    function f(x){
        var power = Math.floor(Math.log(x)/Math.log(5));
        var res = 0;
        for(var i=1;i<=power;i++){
            res += Math.floor(x/(5**i))
        } 
        return res;
    }
};
// console.log(preimageSizeFZF(79))
// console.log(preimageSizeFZF(12))
console.log(preimageSizeFZF(10))
//console.log(preimageSizeFZF(3))
// @lc code=end

