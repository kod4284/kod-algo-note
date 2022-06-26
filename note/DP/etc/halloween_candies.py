A = [5,7,8,10,9,4,2,11,6]

def solution(l):
  if l == 0:
    return A[l]
  if l == 1:
    return A[l]
  return max(solution(l-1), solution(l-2)+ A[l])

print(solution(len(A) -1))