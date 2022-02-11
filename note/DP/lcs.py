# Longest Common Substrinquence

X = "helloworld"
Y = "longwayhome"
n = len(X)
m = len(Y)
T = [[None] * (n + 1) for _ in range(m + 1)]

def init_base_case():
  for i in range(n + 1):
    T[0][i] = 0
  for j in range(1, m + 1):
    T[j][0] = 0

def lcs(X, Y):
  init_base_case()
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if Y[i-1] == X[j-1]:
        T[i][j] = T[i-1][j-1] + 1
      else:
        T[i][j] = max(T[i-1][j], T[i][j-1])
  return T[m][n]

print(lcs(X, Y))
