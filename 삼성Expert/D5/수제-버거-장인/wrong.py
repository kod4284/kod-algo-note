from itertools import combinations
import math

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

cnt = 0
for i in range(0, 2):
    cnt += math.comb(3, i)
print(cnt)
def solve():
    N, M = readline()
    possible_list = [(i) for i in range(1, N + 1)]
    temp = []
    except_list = []
    for _ in range(M):
        a, b = readline()
        except_list.append((a, b))
    for i in range(2, N + 1):
        for j in combinations(possible_list, i):
            temp.append(j)

    new_list = temp + possible_list
    for a, b in except_list:
        for j in new_list:
            if type(j) != int and a in j and b in j:
                new_list.remove(j)

    return len(new_list) + 1
    



TC = read()

for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))