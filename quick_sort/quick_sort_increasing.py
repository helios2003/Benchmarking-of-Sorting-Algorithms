def quick_sort_increasing(arr):
    return _quick_sort(arr, 0, len(arr)-1)

def _quick_sort(arr, start, end):
    if start >= end:
        return arr, 0
    pivot = arr[start]
    i = start + 1
    j = end
    comparisons = 0
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
    _quick_sort(arr, start, j-1)
    _quick_sort(arr, j+1, end)