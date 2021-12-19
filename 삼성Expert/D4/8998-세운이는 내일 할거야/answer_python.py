read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def solve():
    arr = []
    N = read()
    for _ in range(N):
        T, D = readline()
        arr.append((T, D))
    # 두번째 원소로 오름차순 정렬
    arr.sort(key=lambda x: -x[1])
    mini_d = int(1e9)
    for i, tup in enumerate(arr):
        t, d = tup
        if i == 0:
            mini_d = d - t
            continue
        mini_d = min(mini_d, d)
        mini_d -= t
    return mini_d

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))
