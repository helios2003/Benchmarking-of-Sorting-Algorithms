"""
ALGORITHM:
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element 
as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position 
in the sorted array.
"""

# best -> pivot at middle -> sorted with pivot choice 3
# avg -> jumbled woth pivot choice = 2
# worst -> pivot at start or end -> random array with pivot choice = 1

import random

def quick_sort_version1(arr, low, high):
    if low < high:
        pivot = arr[low]
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version1(arr, low, pivot_idx - 1)
        quick_sort_version1(arr, pivot_idx + 1, high)

def quick_sort_version2(arr, low, high):
    if low < high:
        pivot = random.choice(arr[low:high+1])
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version2(arr, low, pivot_idx - 1)
        quick_sort_version2(arr, pivot_idx + 1, high)

def quick_sort_version3(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        candidates = [arr[low], arr[mid], arr[high]]
        candidates.remove(max(candidates))
        candidates.remove(min(candidates))
        pivot = candidates[0]
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version3(arr, low, pivot_idx - 1)
        quick_sort_version3(arr, pivot_idx + 1, high)

def quick_sort_version3(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_version3(arr, low, pi - 1)
        quick_sort_version3(arr, pi + 1, high)

def get_median(arr, low, high):
    mid = (low + high) // 2
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high

def partition(arr, low, high, pivot):
    pivot_index = get_median(arr, low, high)
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]

    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j