'''
各种排序算法实现
'''

# 【冒泡排序】
# 从前向后，相邻两数比较，若逆序就交换。
# 一趟排序可以固定最后一个数，一趟比一趟少比较一个数。
def bubbleSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

# 【选择排序】
# 选择最小的数和最前面的位置交换,一趟排序可以确定当前趟的第一个数
def selectSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

# 【直接插入排序】
# 将下一个数插入到有序数组中
def insertSort(arr):
    if len(arr)<=1:
        return arr
    nums = []
    for n in arr:
        if not nums:
            nums.append(n)
        else:
            i = 0
            while i<len(nums) and n > nums[i]:
                i+=1
            nums.insert(i,n)
    return nums

# 【快速排序】
# 选择pivot，对数组进行左右区间划分，divide and conquer
def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSort(left)+[pivot]+quickSort(right)   

# 【归并排序】
# 不断划分，对子数组进行排序和归并
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        half = int(len(arr)/2)
        left = mergeSort(arr[:half])
        right = mergeSort(arr[half:])
        i,j=0,0
        merged = []
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

# 【堆排序】
# 将数组看成完全二叉树，利用建最小堆的方式来排序
def heapSort(nums):
    arr = nums.copy()
    for k in range(len(nums)): 
        def makeHeap(i):
            if i >= (len(arr)-1)/2:
                return
            makeHeap(2*i+1)
            makeHeap(2*i+2)
            if arr[2*i+1] < arr[i]:
                arr[2*i+1],arr[i] = arr[i],arr[2*i+1]
            if 2*i+2 < len(arr) and  arr[2*i+2] < arr[i]:
                arr[2*i+2],arr[i] = arr[i],arr[2*i+2]
        makeHeap(0)
        nums[k]=arr[0]
        arr = arr[1:]
    return nums
        


if __name__=='__main__':
    arr = [3,2,5,1,8,7,0]
    print(bubbleSort(arr.copy()))
    print(selectSort(arr.copy()))
    print(insertSort(arr.copy()))
    print(quickSort(arr.copy()))
    print(mergeSort(arr.copy()))
    print(heapSort(arr.copy()))
