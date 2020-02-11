/*
 * @lc app=leetcode.cn id=406 lang=javascript
 *
 * [406] 根据身高重建队列
 *
 * https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
 *
 * algorithms
 * Medium (60.77%)
 * Likes:    230
 * Dislikes: 0
 * Total Accepted:    15.9K
 * Total Submissions: 25.7K
 * Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
 *
 * 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
 * 编写一个算法来重建这个队列。
 * 
 * 注意：
 * 总人数少于1100人。
 * 
 * 示例
 * 
 * 
 * 输入:
 * [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
 * 
 * 输出:
 * [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    // 【解法1】，感觉后面部分是可以优化的 O(N^2) 
    // Your runtime beats 7.69 % of javascript submissions
    // Your memory usage beats 100 % of javascript submissions (38.8 MB)
/*     people.sort((a,b)=>{
        if (a[0]!=b[0])
            return a[0]-b[0];
        else{
            return b[1]-a[1];
        }
    });
    var queue = new Array(people.length);
    for(let person of people){
        var k = person[1];
        var i=0;
        while(k>0||queue[i]!=undefined){
            if(queue[i]==undefined)
                k--;
            i++;
        }
        queue[i]=person;
    }
    return queue; */

    // 解法2 利用numbers数组记录位置。
    //Your runtime beats 98.9 % of javascript submissions
    //Your memory usage beats 25.45 % of javascript submissions (40.1 MB) 
    people.sort((a,b)=>{
        if (a[0]!=b[0])
            return a[0]-b[0];
        else{
            return b[1]-a[1];
        }
    });
    var queue = new Array(people.length);
    var number = [...Array(people.length).keys()];
    for(let person of people){
        let k = person[1];
        queue[number[k]]=person;
        number.splice(k,1);
    }
    return queue;

};
// @lc code=end

console.log(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))