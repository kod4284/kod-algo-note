read = lambda: int(input())
readline = lambda: map(int, input().split())

def solve():
    N, K = readline()
    pre_coin, pre_count = readline()

    value, kind = 0, 0

    for _ in range(N - 1):
        coin, count = readline()
        if value + pre_coin < coin and pre_count == 0:
            value += pre_coin
            kind += 1
        pre_coin = coin
        pre_count = count

    if value + pre_coin <= K and pre_count == 0:
        value += pre_coin
        kind += 1
    if kind == 0:
        value = 1
    return "{} {}".format(kind, K - value)
    
# 출력부
TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))