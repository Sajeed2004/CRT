def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        mid = (start + end) // 2
        # Recursively sort the first half
        merge_sort(arr, start, mid)
        # Recursively sort the second half
        merge_sort(arr, mid + 1)
        # Merge the sorted halves
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [30, 12, 4, 49, 45]
merge_sort(arr)
print(arr)