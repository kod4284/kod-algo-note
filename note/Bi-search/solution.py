array = [1, 2, 4, 5, 6, 7, 8, 9, 13, 26, 29]

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)
    

def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    

print(binary_search(array, 1, 0, len(array) - 1))
print(binary_search_while(array, 4, 0, len(array) - 1))