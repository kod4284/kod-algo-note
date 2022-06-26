import pprint

X = "helloworld"
Y = "longwayhome"
# loword
# X = "hello"
# Y = "elo"
# X = "ababcdeabcdefghifghiabcde"
# Y = "a__b__c_d_eee_ffaf_g_habcd_i" #abcdeabcd
# X = "ababcdea"
# Y = "abcdeeeffafg_habcd_i" #abcdeabcd
# X = "ababcdeabcdefghifghiabcde"
# Y = "a__b__c_d_eee_ffaf_g_habcd_i" #abcdeabcd
n = len(X)
m = len(Y)
T = [[None] * (n + 1) for _ in range(m + 1)]

def init_base_case():
  for i in range(n + 1):
    T[0][i] = 0
  for j in range(1, m + 1):
    T[j][0] = 0

# Longest Common Subsequence
def lc_subsequence(X, Y):
  init_base_case()
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if Y[i-1] == X[j-1]:
        T[i][j] = T[i-1][j-1] + 1
      else:
        T[i][j] = max(T[i-1][j], T[i][j-1])
  return T[m][n]

# Longest Common Substrinquence
def lc_substrinquence(X, Y):
  init_base_case()
  l_i, l_j, data = 0, 0, 0
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if Y[i-1] == X[j-1]:
        T[i][j] = T[i-1][j-1] + 1
      else:
        T[i][j] = T[i-1][j]
      if T[l_i][l_j] < T[i][j]:
        l_i, l_j = i, j
  length = T[l_i][l_j]
  return X[l_j - length : l_j]

print(lc_substrinquence(X, Y))
# pprint.pprint(T)
