/*
 * @lc app=leetcode.cn id=319 lang=javascript
 *
 * [319] 灯泡开关
 *
 * https://leetcode-cn.com/problems/bulb-switcher/description/
 *
 * algorithms
 * Medium (43.56%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    7.4K
 * Total Submissions: 16.8K
 * Testcase Example:  '3'
 *
 * 初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3
 * 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。
 * 找出 n 轮后有多少个亮着的灯泡。
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出: 1 
 * 解释: 
 * 初始时, 灯泡状态 [关闭, 关闭, 关闭].
 * 第一轮后, 灯泡状态 [开启, 开启, 开启].
 * 第二轮后, 灯泡状态 [开启, 关闭, 开启].
 * 第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 
 * 
 * 你应该返回 1，因为只有一个灯泡还亮着。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    // 思路1
    // 如果n不大的话，可以用位运算吧……
    // if( n==0 )
    //     return 0
    // var base = 0;
    // for(let i=1;i<=n;i++){
    //     for(let j=i-1;j<n;j+=i)
    //         base = base^(1<<j)
    // }
    // var count = 0;
    // while(base){
    //     count++;
    //     base = base&(base-1)
    // }
    // return count;

    // 思路2，所有数都翻它的因子个数次，只有平方数是奇数次会翻到亮，其他都会关掉。
    return Math.floor(Math.sqrt(n))
};
// @lc code=end

