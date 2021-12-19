# 핵심: 가격이 높은 순서대로 탐색해야함
read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

N = read()

board = [[False] * (N + 1) for _ in range(N + 1)]
except_days = []
pay = {}
cases = []

def do_or(board_a, board_b):
    r = []
    for i in range(N + 1):
        r.append(board_a[i] | board_b[i])
    return r

# 초기화
for i in range(1, N + 1):
    T, P = readline()
    cases.append((i, P))
    pay[i] = P
    interv = i + T - 1
    for j in range(i, interv + 1):
        if j > N:
            except_days.append(i)
            break
        board[i][j] = True
cases.sort(key=lambda x: -x[1])

result = []
for i in range(1, N + 1):
    ans = []
    nb = board[i]
    if i in except_days:
        result.append([])
        continue
    for j, _ in cases:
        if j in except_days:
            continue
        for k in range(1, N + 1):
            if nb[k] & board[j][k]:
                break
        else:
            nb = do_or(nb, board[j])
            ans.append(j)
    result.append([i] + ans)

ans = []
for r in result:
    s = 0
    for i in r:
        s += pay[i]
    ans.append(s)
print(max(ans))