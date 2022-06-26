from pprint import pprint
A = [3, 4, 5]
K = 8

# Top-Down
# def counting_combos(A, N, W):
#   if W == 0:
#     return 1

#   if N == 0:
#     return 0
  
#   if A[N-1] > W:
#     return counting_combos(A, N-1, W)
#   else:
#     return counting_combos(A, N-1, W) + counting_combos(A, N-1, W - A[N-1])

# print(counting_combos(A, len(A), K))

T = [[None] * (K + 1) for _ in range(len(A) + 1)]

# row: i
# col: k (W)
def init_basecase():
  for i in range(K + 1):
    T[0][i] = 0
  for i in range(len(A) + 1):
    T[i][0] = 1

def counting_combos(A, N, W):
  init_basecase()
  for i in range(1, len(A)+1):
    for j in range(1, K+1):
      if j - A[i-1] >= 0:
        T[i][j] = T[i-1][j] + T[i-1][j - A[i-1]]
      else:
        T[i][j] = T[i-1][j]

counting_combos(A, len(A), K)
pprint(T)