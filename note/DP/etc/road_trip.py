import math

C = [100, 250, 400]
P = [12, 20, 3]
n = len(C)
T = [math.inf] * (n+1)

def init_basecases():
  T[0] = 0
  for i in range(1, len(T)):
    if C[i-1] <= 300:
      T[i] = P[i-1]

def road_trip(N):
  init_basecases()
  for i in range(n - 1):
    for j in range(i + 1, n):
      if C[j] - C[i] <= 300:
        T[j+1] = min(T[j+1], T[i+1]+P[j])
      else:
        break
  return T[N]

print(road_trip(3))