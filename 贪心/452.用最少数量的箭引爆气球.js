/*
 * @lc app=leetcode.cn id=452 lang=javascript
 *
 * [452] 用最少数量的箭引爆气球
 *
 * https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
 *
 * algorithms
 * Medium (47.09%)
 * Likes:    83
 * Dislikes: 0
 * Total Accepted:    7.9K
 * Total Submissions: 16.2K
 * Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
 *
 * 
 * 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在10^4个气球。
 * 
 * 一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart
 * ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
 * 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
 * 
 * Example:
 * 
 * 
 * 输入:
 * [[10,16], [2,8], [1,6], [7,12]]
 * 
 * 输出:
 * 2
 * 
 * 解释:
 * 对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    // 优化的话，排完序遍历的时候，只要记前一个的区间就好了，如果后一个和它无交集count++
    //Your runtime beats 18.18 % of javascript submissions
    //Your memory usage beats 5.41 % of javascript submissions (46.6 MB)
    points.sort((a,b)=>{
        return a[0]-b[0];
    })
    var intervals = points.reduce(((merged,cur,i)=>{
        if(merged.length==0)
            return [cur]
        else{
            let prev = merged.pop();
            if(cur[0]>prev[1]){
                merged.push(prev)
                merged.push(cur);
            }else{
                let intersection = [cur[0],Math.min(cur[1],prev[1])]
                merged.push(intersection);
            }
            return merged;
        }
    }),[])
    return intervals.length
};
// @lc code=end

console.log(findMinArrowShots([]))
