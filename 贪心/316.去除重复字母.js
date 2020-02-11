/*
 * @lc app=leetcode.cn id=316 lang=javascript
 *
 * [316] 去除重复字母
 *
 * https://leetcode-cn.com/problems/remove-duplicate-letters/description/
 *
 * algorithms
 * Hard (35.61%)
 * Likes:    97
 * Dislikes: 0
 * Total Accepted:    6.5K
 * Total Submissions: 17.5K
 * Testcase Example:  '"bcabc"'
 *
 * 给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
 * 
 * 示例 1:
 * 
 * 输入: "bcabc"
 * 输出: "abc"
 * 
 * 
 * 示例 2:
 * 
 * 输入: "cbacdcbc"
 * 输出: "acdb"
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    if(s.length<=1) return s;
    var stack=[];
    var counter={};
    var used={}
    for(let i=0;i<s.length;i++){
        if(s[i] in counter){
            counter[s[i]]++;
        }else{
            counter[s[i]]=1;
        }
    }
    for(let i=0;i<s.length;i++){
        if(stack.length==0){
            stack.push(s[i])
            counter[s[i]]--;
            used[s[i]]=true
        }else {
            if(used[s[i]]){
                counter[s[i]]--;
                continue
            } 
            while(stack.length>0){
                let tail = stack.pop();
                used[tail]=false
                if(tail.charCodeAt(0)<s[i].charCodeAt(0)||counter[tail]==0){
                    stack.push(tail);
                    used[tail]=true
                    break
                }
            }
            stack.push(s[i]);
            used[s[i]]=true
            counter[s[i]]--;
            
        }
    }
    console.log(stack.join(''))
    return stack.join('');
};

// @lc code=end

removeDuplicateLetters("bbcaac")
removeDuplicateLetters("cbacdcbc")
removeDuplicateLetters("kaefabbdfce")