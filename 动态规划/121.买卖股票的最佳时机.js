/*
 * @lc app=leetcode.cn id=121 lang=javascript
 *
 * [121] 买卖股票的最佳时机
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
 *
 * algorithms
 * Easy (51.51%)
 * Likes:    721
 * Dislikes: 0
 * Total Accepted:    122.3K
 * Total Submissions: 234.2K
 * Testcase Example:  '[7,1,5,3,6,4]'
 *
 * 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
 * 
 * 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
 * 
 * 注意你不能在买入股票前卖出股票。
 * 
 * 示例 1:
 * 
 * 输入: [7,1,5,3,6,4]
 * 输出: 5
 * 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
 * ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [7,6,4,3,1]
 * 输出: 0
 * 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {    
/* // O(n^2)时间
   // Your runtime beats 19.34 % of javascript submissions
   // Your memory usage beats 73.12 % of javascript submissions (35.4 MB)  
    var profit=0;
    for(let i=0;i<prices.length-1;i++){
        for(let j=i+1;j<prices.length;j++){
            if(prices[j]-prices[i]>profit)
                profit = prices[j]-prices[i]
        }
    }
    return profit
 */

    // DP O(n)时间 O(1)空间
    // Your runtime beats 97.37 % of javascript submissions
    // Your memory usage beats 42.24 % of javascript submissions (35.5 MB)
    if(prices.length==0) return []
    var min=prices[0];
    var profit=0;
    for(let i=0;i<prices.length;i++){
        min = Math.min(prices[i],min)
        profit = Math.max(prices[i]-min,profit)
    }
    return profit
};
// @lc code=end

console.log(maxProfit([7,1,5,3,6,4]))
console.log(maxProfit([7,3,6,1,9,2]))
