from typing import List

def merge_sort(arr: List[int]) -> list[int]:
  n = len(arr)
  if n > 1:
    return merge(merge_sort(arr[:n//2]), merge_sort(arr[n//2:]))
  else:
    return arr[:]

def merge(x: List[int], y: List[int]) -> List[int]:
  k = len(x)
  l = len(y)
  if k == 0:
    return y[:l]
  if l == 0:
    return x[:k]
  if x[0] <= y[0]:
    return [x[0]] + merge(x[1:k], y[0:l])
  else:
    return [y[0]] + merge(x[0:k], y[1:l])
  
arr = [10, 2, 5, 3, 7, 12, 1, 6]
print(merge_sort(arr))