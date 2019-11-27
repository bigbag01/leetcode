/*
 * @lc app=leetcode id=4 lang=javascript
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (25.48%)
 * Total Accepted:    382.5K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * 
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * Example 1:
 * 
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * The median is 2.0
 * 
 * 
 * Example 2:
 * 
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * The median is (2 + 3)/2 = 2.5
 * 
 * 
 */
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    var combined=[];
    var i=0,j=0;
    while(i<nums1.length&&j<nums2.length){
        if(nums1[i]<nums2[j]){
            combined.push(nums1[i]);
            i++;
        }else{
            combined.push(nums2[j]);
            j++;
        }
    }
    for(;i<nums1.length;i++){
        combined.push(nums1[i]);
    }
    for(;j<nums2.length;j++){
        combined.push(nums2[j])
    }
    console.log(combined);
    if(combined.length%2){
        return combined[Math.floor(combined.length/2)];
    }else{
        return (combined[combined.length/2]+combined[combined.length/2-1])/2
    }
};

