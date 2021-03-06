/*
 * @lc app=leetcode.cn id=464 lang=javascript
 *
 * [464] 我能赢吗
 *
 * https://leetcode-cn.com/problems/can-i-win/description/
 *
 * algorithms
 * Medium (33.03%)
 * Likes:    77
 * Dislikes: 0
 * Total Accepted:    2.6K
 * Total Submissions: 7.7K
 * Testcase Example:  '10\n11'
 *
 * 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。
 * 
 * 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
 * 
 * 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
 * 
 * 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数
 * desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
 * 
 * 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
 * 
 * 示例：
 * 
 * 输入：
 * maxChoosableInteger = 10
 * desiredTotal = 11
 * 
 * 输出：
 * false
 * 
 * 解释：
 * 无论第一个玩家选择哪个整数，他都会失败。
 * 第一个玩家可以选择从 1 到 10 的整数。
 * 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
 * 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
 * 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} maxChoosableInteger
 * @param {number} desiredTotal
 * @return {boolean}
 */
var canIWin = function(maxChoosableInteger, desiredTotal) {
    if(maxChoosableInteger>desiredTotal)
        return true;
    if((1+maxChoosableInteger)*maxChoosableInteger/2<desiredTotal)
        return false;
    
    var status={};
    function win(maxNum,total,visited){
        if(visited in status){
            return status[visited];
        }
        for(let i=1;i<=maxNum;i++){
            let cur = 1<<i;
            if((visited&cur)==0){
                if(i>=total||!win(maxNum,total-i,visited|cur)){
                    status[visited] = true;
                    return true
                }
            }
        }
        status[visited] = false;
        return false;
    }
    return win(maxChoosableInteger,desiredTotal,0);
};
// @lc code=end

console.log(canIWin(10,11))
