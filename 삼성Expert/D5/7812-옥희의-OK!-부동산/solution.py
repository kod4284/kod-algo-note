readline = lambda: list(map(int, input().split()))

def solve():
    N, M = readline()
    arr = readline()

    end = 0
    sumv = 0
    cnt = 0

    for start in range(N):
        while end < N and sumv < M:
            sumv += arr[end]
            end += 1
        if sumv == M:
            cnt += 1
        sumv -= arr[start]
    return cnt

TC = int(input())
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))