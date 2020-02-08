/*
 * @lc app=leetcode.cn id=714 lang=javascript
 *
 * [714] 买卖股票的最佳时机含手续费
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
 *
 * algorithms
 * Medium (58.76%)
 * Likes:    124
 * Dislikes: 0
 * Total Accepted:    9.6K
 * Total Submissions: 15.8K
 * Testcase Example:  '[1,3,2,8,4,9]\n2'
 *
 * 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
 * 
 * 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
 * 
 * 返回获得利润的最大值。
 * 
 * 示例 1:
 * 
 * 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
 * 输出: 8
 * 解释: 能够达到的最大利润:  
 * 在此处买入 prices[0] = 1
 * 在此处卖出 prices[3] = 8
 * 在此处买入 prices[4] = 4
 * 在此处卖出 prices[5] = 9
 * 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
 * 
 * 注意:
 * 
 * 
 * 0 < prices.length <= 50000.
 * 0 < prices[i] < 50000.
 * 0 <= fee < 50000.
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    if (prices.length<=1) return 0

    var prev;
    var merged = prices.reduce((ranges,cur)=>{
        if(prev!=undefined){
            if(cur-prev>fee){
                ranges.push([prev,cur])
                prev=undefined; 
            }else{
                prev = Math.min(prev,cur)
            }    
        }else{
            if(ranges.length==0)
                prev=cur
            else{
                let cur_range = ranges[ranges.length-1];
                if (cur_range[1]<cur){
                    ranges[ranges.length-1][1]=cur
                }
                else if (cur_range[1]-cur>fee){
                    prev = cur
                }
            }
        }
        return ranges
    },[])
    

    return merged.reduce((total,cur)=>{
        return total+cur[1]-cur[0]
    },0)-merged.length*fee;
};
// @lc code=end

// console.log(maxProfit([1, 3, 2, 8, 4, 9],2))
// console.log(maxProfit([1,2,3,4,5],1))
// console.log(maxProfit([4,3,2,6,7,10,0,5],4))