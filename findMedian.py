random = [5,3,1,2,4]

def findMedian(arr):
    arr.sort()
    mid = len( arr ) // 2
    return arr[ mid ]