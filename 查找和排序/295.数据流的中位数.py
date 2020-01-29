#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (40.58%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 21.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        维护一个最大堆和一个最小堆，添加数的同时保证两边数量相差<=1
        18/18 cases passed (276 ms)
        Your runtime beats 37.53 % of python3 submissions
        Your memory usage beats 57.79 % of python3 submissions (24.3 MB)
        """
        import heapq
        self.big_endian = []
        self.small_endian = []

    def addNum(self, num: int) -> None:
        import heapq
        if len(self.small_endian) == 0:
            heapq.heappush(self.small_endian,num)
        # elif len(self.big_endian) == 0:
        #     heapq.heappush(self.big_endian,-num)
        else:
            med = self.findMedian()
            if num > med:
                heapq.heappush(self.small_endian,num)
            else:
                heapq.heappush(self.big_endian,-num)
            if len(self.big_endian)-len(self.small_endian)>1:
                item = heapq.heappop(self.big_endian)
                heapq.heappush(self.small_endian,-item)
            elif len(self.small_endian)-len(self.big_endian)>1:
                item = heapq.heappop(self.small_endian)
                heapq.heappush(self.big_endian,-item)

    def findMedian(self) -> float:
        import heapq
        if len(self.big_endian)-len(self.small_endian) == 1:
            return -self.big_endian[0]
        elif len(self.big_endian)-len(self.small_endian) == -1:
            return self.small_endian[0]
        else:
            return (self.small_endian[0]-self.big_endian[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# print(obj.findMedian())
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
# obj.addNum(6)
# obj.addNum(0)
# print(obj.findMedian())
# obj.addNum(11)
# obj.addNum(5)
# print(obj.findMedian())
# @lc code=end

