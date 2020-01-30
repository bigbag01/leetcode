#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (39.45%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    33.5K
# Total Submissions: 83.5K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#

# @lc code=start
class Solution:
    def exist(self, board, path) :
        if not board:
            if not path:
                return True
            else:
                return False
        rows = len(board)
        cols = len(board[0])
        if rows*cols < len(path):
            return False
        if not path:
            return True
        def checkPath(i,j,subpath,visited):

            if not subpath:
                return True
            else:
                if i >= 0 and i < rows and j >= 0 and j < cols and board[i][j]==subpath[0] and not visited.get(i*cols+j,False):
                    visited[i*cols+j]=True
                    top = checkPath(i-1,j,subpath[1:],visited)
                    bottom = checkPath(i+1,j,subpath[1:],visited)
                    left = checkPath(i,j-1,subpath[1:],visited) 
                    right = checkPath(i,j+1,subpath[1:],visited)
                    if top or bottom or left or right:
                        #print(i,j)
                        return True
                    else:
                        visited[i*cols+j] = False
                return False
            
        
        for i in range(rows):
            for j in range(cols):
                visited = {}
                if checkPath(i,j,path,visited):
                    return True
        return False
        
# @lc code=end
sol = Solution()
# print(sol.exist([
#   ['A','B','C','E','H','J','I','G'],
#   ['S','F','C','S','L','O','P','Q'],
#   ['A','D','E','E','M','N','O','E'],
#   ['A','D','I','D','E','J','F','M'],
#   ['V','C','E','I','F','G','G','S']
# ],"SGGFIECVAASABCEHJIGQEM"))

# print(sol.exist([
#     ["A","B","C","E"],
#     ["S","F","E","S"],
#     ["A","D","E","E"]
# ],"ABCESEEEFS"))

print(sol.exist([
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"]
    ],"aaaaaaaaaaaaa"))