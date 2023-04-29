def quick_sort_median(arr):
    return _quick_sort(arr, 0, len(arr)-1)

def _quick_sort(arr, start, end):
    if start >= end:
        return arr, 0
    comparisons = 0
    pivot_index = _get_pivot_index(arr, start, end)
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    pivot = arr[start]
    i = start + 1
    j = end
    while i <= j:
        if arr[i] <= pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            comparisons += 1
    arr[start], arr[j] = arr[j], arr[start]
    left_arr, left_comp = _quick_sort(arr, start, j-1)
    right_arr, right_comp = _quick_sort(arr, j+1, end)
    return arr, comparisons + left_comp + right_comp

def _get_pivot_index(arr, start, end):
    mid = (start + end) // 2
    if arr[start] < arr[mid]:
        if arr[mid] < arr[end]:
            return mid
        elif arr[start] < arr[end]:
            return end
        else:
            return start
    else:
        if arr[end] < arr[mid]:
            return mid
        elif arr[end] < arr[start]:
            return end
        else:
            return start
