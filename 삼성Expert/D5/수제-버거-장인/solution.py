read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def solve():
    N, M = readline()
    except_set = set()
    for i in range(M):
        a, b = readline()
        except_set.add((2 ** (a - 1)) + (2 ** (b - 1)))
    cnt = 0
    for i in range(2 ** N):
        for s in except_set:
            if s & i == s:
                break
        else:
            cnt += 1
    return cnt

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))