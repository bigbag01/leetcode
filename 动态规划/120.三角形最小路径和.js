/*
 * @lc app=leetcode.cn id=120 lang=javascript
 *
 * [120] 三角形最小路径和
 *
 * https://leetcode-cn.com/problems/triangle/description/
 *
 * algorithms
 * Medium (62.62%)
 * Likes:    302
 * Dislikes: 0
 * Total Accepted:    38.5K
 * Total Submissions: 60.6K
 * Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
 *
 * 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
 * 
 * 例如，给定三角形：
 * 
 * [
 * ⁠    [2],
 * ⁠   [3,4],
 * ⁠  [6,5,7],
 * ⁠ [4,1,8,3]
 * ]
 * 
 * 
 * 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
 * 
 * 说明：
 * 
 * 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
 * 
 */

// @lc code=start
/**
 * @param {number[][]} triangle
 * @return {number}
 */
// Time Limit Exceeded
/* var minimumTotal = function(triangle) {
    
    function helper(i,j){
        if(i>=triangle.length||j>=triangle[i].length){
            return 0
        }else{
            return triangle[i][j]+Math.min(helper(i+1,j),helper(i+1,j+1))
        }
    }
    return helper(0,0);
}; */
var minimumTotal = function(triangle){
    // Your runtime beats 67 % of javascript submissions
    // Your memory usage beats 88.08 % of javascript submissions (34.7 MB)
    var n=triangle.length;
    if(n==0) return 0;
    for(let i = n - 2 ; i >= 0; i--){
        for(let j=0;j<=i;j++){
            triangle[i][j]=triangle[i][j]+Math.min(triangle[i+1][j],triangle[i+1][j+1]);
        }
    }
    return triangle[0][0]
}





// @lc code=end

console.log(minimumTotal([
    [2],
   [3,4],
  [6,5,7],
 [4,1,8,3]
]))
console.log(minimumTotal([]))
console.log(minimumTotal([[1]]))