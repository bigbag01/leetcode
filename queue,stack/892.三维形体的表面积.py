#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积

# Your runtime beats 59.79 % of python3 submissions
# Your memory usage beats 6 % of python3 submissions (13.9 MB)


# @lc code=start
class Solution:
    # 思路：
    # 一叠v个立方体的表面积是4*v+2
    # 相邻两叠需要减去 min(v1,v2)*2个面
    # 求个和和差就出来结果了
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        overlap = 0
        if len(grid) == 0:
            return 0
        L = len(grid)
        W = len(grid[0])
        for i in range(L):
            for j in range(W):
                v = grid[i][j]
                if v > 0:
                    surface += 4*v+2
                if j+1 < W:
                    overlap += min(v,grid[i][j+1])*2
                if i+1 < L:
                    overlap += min(v,grid[i+1][j])*2
        return surface-overlap
# @lc code=end

