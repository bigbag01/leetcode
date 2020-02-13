/*
 * @lc app=leetcode.cn id=152 lang=javascript
 *
 * [152] 乘积最大子序列
 *
 * https://leetcode-cn.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (36.08%)
 * Likes:    362
 * Dislikes: 0
 * Total Accepted:    31.8K
 * Total Submissions: 86.7K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
 * 
 * 示例 1:
 * 
 * 输入: [2,3,-2,4]
 * 输出: 6
 * 解释: 子数组 [2,3] 有最大乘积 6。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [-2,0,-1]
 * 输出: 0
 * 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var max,imax=1,imin=1;
    
    for(num of nums){
        if(num<0){
            imax = imax^imin;
            imin = imax^imin;
            imax = imax^imin;
        }
        imax = Math.max(imax*num,num);
        imin = Math.min(imin*num,num);
        
        if(max==undefined||max<imax)
            max = imax;

    }
    return max;
};

// @lc code=end

console.log(maxProduct([2,3,-2,4]))
console.log(maxProduct([-2,0,-1]))
console.log(maxProduct([-1]))
console.log(maxProduct([0]))
console.log(maxProduct([2,3,-2,3,4,-1,0,3,5,-1,6]))
console.log(maxProduct([2,-5,-2,-4,3]))