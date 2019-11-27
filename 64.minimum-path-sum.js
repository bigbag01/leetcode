/*
 * @lc app=leetcode id=64 lang=javascript
 *
 * [64] Minimum Path Sum
 *
 * https://leetcode.com/problems/minimum-path-sum/description/
 *
 * algorithms
 * Medium (45.42%)
 * Total Accepted:    208K
 * Total Submissions: 457.8K
 * Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
 *
 * Given a m x n grid filled with non-negative numbers, find a path from top
 * left to bottom right which minimizes the sum of all numbers along its path.
 * 
 * Note: You can only move either down or right at any point in time.
 * 
 * Example:
 * 
 * 
 * Input:
 * [
 * [1,3,1],
 * ⁠ [1,5,1],
 * ⁠ [4,2,1]
 * ]
 * Output: 7
 * Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 * 
 * 
 */
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {

    for(var i=0;i<grid.length;i++){
        for(var j=0;j<grid[0].length;j++){
            if(i==0&&j!=0)
                grid[i][j]=grid[i][j-1]+grid[i][j];
            else if(i!=0&&j==0)
                grid[i][j]=grid[i-1][j]+grid[i][j];
            else if(i!=0&&j!=0)
                grid[i][j]=grid[i][j]+Math.min(grid[i][j-1],grid[i-1][j])
        }
    }
    return grid[grid.length-1][grid[0].length-1];
};

