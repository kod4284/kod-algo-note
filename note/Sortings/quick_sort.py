from typing import List

def quick_sort(arr: List[int], start, end):
  if start >= end:
    return 
  pivot = end
  left = start
  right = end - 1
  while left <= right:
    while arr[left] <= arr[pivot] and left < end:
      left += 1
    while arr[right] > arr[pivot] and start <= right:
      right -= 1
    if left > right:
      arr[pivot], arr[left] = arr[left], arr[pivot]
    else:
      arr[left], arr[right] = arr[right], arr[left]
  quick_sort(arr, start, left-1)
  quick_sort(arr, left + 1, end)

arr = [10, 2, 5, 3, 7, 12, 1, 6]
print(quick_sort(arr, 0, len(arr) - 1))
print(arr)
