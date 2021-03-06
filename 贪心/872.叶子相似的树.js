/*
 * @lc app=leetcode.cn id=872 lang=javascript
 *
 * [872] 叶子相似的树
 *
 * https://leetcode-cn.com/problems/leaf-similar-trees/description/
 *
 * algorithms
 * Easy (61.23%)
 * Likes:    47
 * Dislikes: 0
 * Total Accepted:    8.9K
 * Total Submissions: 14.4K
 * Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
 *
 * 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
 * 
 * 
 * 
 * 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
 * 
 * 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
 * 
 * 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 给定的两颗树可能会有 1 到 100 个结点。
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.*/
/* function TreeNode(val) {
    this.val = val;
    this.left=this.right=null;
} */

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    return traverse(root1).join(',')==traverse(root2).join(',')
};
function traverse(node){
    if(node==null)
        return []
    if (node.left==null&&node.right==null){
        return [node.val]
    }else{
        return [].concat(traverse(node.left),traverse(node.right));
    }
}
// @lc code=end


var root = TreeNode(0);
var root2 = TreeNode(0);
console.log(leafSimilar(root,root2))
debugger