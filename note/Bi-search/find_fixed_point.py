  # [ 0, 1, 2, 3, 4, 5, 6, 7 ]
A = [-3, 0, 1, 2, 4, 6, 7, 11]

def binary_search(arr, target, i, j):
  if i > j:
    return -1
  mid = (i + j) // 2
  if arr[mid] == target:
    return mid
  if arr[mid] > target:
    return binary_search(arr, target, i, mid - 1)
  else:
    return binary_search(arr, target, mid + 1, j)

def find_fixed_point(arr, i, j):
  if i > j:
    return -1
  mid = (i + j) // 2
  if arr[mid] == mid:
    return mid
  if arr[mid] > mid:
    return find_fixed_point(arr, i, mid - 1)
  else:
    return find_fixed_point(arr, mid + 1, j)

# print(binary_search(A, 121, 0, len(A) - 1))
print(find_fixed_point(A, 0, len(A) - 1))