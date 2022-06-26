import math

C = [100, 250, 400, 450, 500]
P = [12, 20, 3, 40, 30]
n = len(C)
T = [math.inf] * n

def init_basecases():
  for i in range(len(T)):
    if C[i] <= 300:
      T[i] = P[i]

def road_trip(N):
  init_basecases()
  for i in range(n - 1):
    for j in range(i + 1, n):
      if C[j] - C[i] <= 300:
        T[j] = min(T[j], T[i]+P[j])
      else:
        break
  return T[N-1]
print(road_trip(3))
print(T)