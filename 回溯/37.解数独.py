#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (58.08%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 29.9K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        Your runtime beats 97.74 % of python3 submissions
        Your memory usage beats 58.56 % of python3 submissions (13.2 MB)
        """
        
        def solve(board):
            modified = [] # 记录当前尝试修改的位置
            candidates = [[set() for i in range(9)] for j in range(9)]
            full = set(['1','2','3','4','5','6','7','8','9'])
            rows = [set() for i in range(9)]
            cols = [set() for i in range(9)]
            boxes = [set() for i in range(9)]
            filled = 0
            for i in range(9):
                for j in range(9):
                    if board[i][j]!='.':
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        boxes[int(i/3)*3+int(j/3)].add(board[i][j])
                        filled += 1
            rows = [full.difference(s) for s in rows]
            cols = [full.difference(s) for s in cols]
            boxes = [full.difference(s) for s in boxes]
            least_cand = 9
            start_pos = None
            while True:
                least_cand = 9
                for i in range(9):
                    for j in range(9):
                        if board[i][j]!='.':
                            continue
                        candidates[i][j] = rows[i].intersection(cols[j]).intersection(boxes[int(i/3)*3+int(j/3)])
                        if len(candidates[i][j])==0:
                            # 当前尝试产生矛盾，返回
                            return filled,modified
                        if len(candidates[i][j])<least_cand:
                            # 记录候选集最小的位置
                            least_cand = len(candidates[i][j])
                            start_pos = (i,j)
                        if len(candidates[i][j])==1:
                            # 如果候选集只有一个，就直接填进去
                            board[i][j] = candidates[i][j].pop()
                            modified.append((i,j))
                            filled += 1
                            rows[i].remove(board[i][j])
                            cols[j].remove(board[i][j])
                            boxes[int(i/3)*3+int(j/3)].remove(board[i][j])       
                if filled == 81 or least_cand!=1:
                    # 如果已经填满或者最小的候选集也大于1就结束当前循环
                    break
            if filled == 81:
                # 已经填满，返回函数
                return filled,modified
            else:
                # 对候选集进行尝试，采用回溯
                i,j = start_pos
                for tmp in list(candidates[i][j]):
                    board[i][j] = tmp
                    modified.append((i,j))
                    nums,recover = solve(board)
                    if nums == 81:
                        return 81,recover
                    else:
                        # 如果返回的nums不为81，说明尝试失败，需要回溯，重新恢复这一次尝试修改的位置
                        for pairs in recover:
                            board[pairs[0]][pairs[1]]='.'
                return filled,modified
        solve(board)

# @lc code=end
sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(board)
