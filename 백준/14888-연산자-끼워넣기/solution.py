from itertools import permutations

readline = lambda: list(map(int, input().split()))
N = int(input())
A = readline()
O = readline()
s = set()
ops = []

for i, o in enumerate(O):
    for _ in range(o):
        if i == 0:
            ops.append("+")
        elif i == 1:
            ops.append("-")
        elif i == 2:
            ops.append("*")
        else:
            ops.append("//")

c = permutations(ops, N - 1)
for i in c:
    s.add(i)
ans = []
for i in s:
    sum_value = A[0]
    for idx, j in enumerate(i):
        if j == "+":
            sum_value += A[idx + 1] 
        elif j == "-":
            sum_value -= A[idx + 1]
        elif j == "*":
            sum_value *= A[idx + 1]
        else:
            if sum_value < 0:
                sum_value = -(-sum_value // A[idx + 1])
            else:
                sum_value //= A[idx + 1]
    ans.append(sum_value)

print(max(ans))
print(min(ans))