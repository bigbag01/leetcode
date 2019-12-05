#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
# Your runtime beats 56.51 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def leastInterval(self, tasks, n):
        cnt_map={}
        for task in tasks:
            cnt_map[task] = cnt_map.get(task,0)+1
        counts = list(cnt_map.values())
        counts.sort(reverse=True)
        vacancy = (counts[0]-1)*n
        for i in range(1,len(counts)):
            cnt = counts[i]
            vacancy -= min(cnt,counts[0]-1)
        if vacancy >0 :
            return len(tasks)+vacancy
        else:
            return len(tasks)
# @lc code=end

ss = Solution()
print(ss.leastInterval(["A","A","A","B","B","B"],2))