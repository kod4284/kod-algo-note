readline = lambda: list(map(int, input().split()))
prime_nums = [2, 3, 5, 7, 11, 13, 17]
comb = [[0] * 20 for _ in range(20)]

TC = int(input())

def init_comb():
    for i in range(20):
        comb[i][0] = 1
        comb[i][i] = 1
    for i in range(2, 20):
        for j in range(1, 20):
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]


def make_prob(p, n, r):
    p = p / 100
    total = p
    cnt = 1
    for _ in range(1, n):
        if cnt >= r:
            total *= (1 - p)
        else:
            total *= p
        cnt += 1
    return total

def solve():
    a, b = readline()
    prob_a = 0
    prob_b = 0
    for i in prime_nums:
        case = comb[18][i]
        prob_a += case * make_prob(a, 18, i)
        prob_b += case * make_prob(b, 18, i)
    return 1 - ((1 - prob_a) * (1 - prob_b))

init_comb()
for i in range(1, TC + 1):
    print("#{} {:.6f}".format(i, round(solve(), 6)))
    