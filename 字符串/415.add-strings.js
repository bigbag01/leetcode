/*
 * @lc app=leetcode id=415 lang=javascript
 *
 * [415] Add Strings
 *
 * https://leetcode.com/problems/add-strings/description/
 *
 * algorithms
 * Easy (42.98%)
 * Total Accepted:    83.8K
 * Total Submissions: 195K
 * Testcase Example:  '"0"\n"0"'
 *
 * Given two non-negative integers num1 and num2 represented as string, return
 * the sum of num1 and num2.
 * 
 * Note:
 * 
 * The length of both num1 and num2 is < 5100.
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to
 * integer directly.
 * 
 * 
 */
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    if(num1.length>num2.length){
        num2=num2.padStart(num1.length,'0')
    }else{
        num1=num1.padStart(num2.length,'0')
    }
    var sum='';
    var i=num1.length-1;
    var remain=0;
    var digit_sum=0;
    while(i>=0){
        digit_sum=Number(num1[i])+Number(num2[i])+remain;
        sum=digit_sum%10+sum;
        remain=Math.floor(digit_sum/10);
        i--;
    }
    if(remain!=0){
        sum=remain+sum;
    }
    return sum;
};

