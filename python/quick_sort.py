from typing import List

def partition(arr: List[int], left: int, right: int) -> int:
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[right]) = (arr[right], arr[i+1])
    return i + 1
    

def quick_sort_r(arr: List[int], left: int, right: int):
    if left < right:
        pivot_position = partition(arr, left, right)
        quick_sort_r(arr, left, pivot_position - 1)
        quick_sort_r(arr, pivot_position + 1, right)

def quick_sort(arr: List[int]) -> List[int]:
    quick_sort_r(arr, 0, len(arr) - 1)
    print(arr)


print(quick_sort([4,3,2,1]))
print(quick_sort([55, 15, 23, 117, 87, 6, 10]))