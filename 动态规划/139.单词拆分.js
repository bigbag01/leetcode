/*
 * @lc app=leetcode.cn id=139 lang=javascript
 *
 * [139] 单词拆分
 *
 * https://leetcode-cn.com/problems/word-break/description/
 *
 * algorithms
 * Medium (42.66%)
 * Likes:    300
 * Dislikes: 0
 * Total Accepted:    33.3K
 * Total Submissions: 77.2K
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
 * 
 * 说明：
 * 
 * 
 * 拆分时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 * 
 * 
 * 示例 1：
 * 
 * 输入: s = "leetcode", wordDict = ["leet", "code"]
 * 输出: true
 * 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
 * 
 * 
 * 示例 2：
 * 
 * 输入: s = "applepenapple", wordDict = ["apple", "pen"]
 * 输出: true
 * 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
 * 注意你可以重复使用字典中的单词。
 * 
 * 
 * 示例 3：
 * 
 * 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出: false
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
// 递归，时间
// Your runtime beats 5.5 % of javascript submissions
// Your memory usage beats 25.35 % of javascript submissions (37.1 MB)
/* var wordBreak = function(s, wordDict) {
    if(s=='') return true;
    for(let word of wordDict){
        var index = s.indexOf(word)
        if (index==-1)
            continue
        else{
            let flag = true;
            for(let ss of s.split(word)){
                flag &= wordBreak(ss,wordDict)
            }
            if(flag) return true
        }
    }
    return false;
}; */


// @lc code=end

console.log(wordBreak("leetcode",['leet','code']))
console.log(wordBreak("applepenapple",["apple", "pen"]))
console.log(wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))
console.log(wordBreak('ccbb',['bc','cb']))