def linear_search(arr, target):
    # Your code here
    index = 0
    for i in arr:
        if i == target:
            return index
        index += 1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    position = -1

    while start <= end:
        if arr[mid] == target:
            position = mid
            break
        
        if target > arr[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2

    return (position)