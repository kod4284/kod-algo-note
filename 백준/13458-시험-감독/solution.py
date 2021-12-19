read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

N = read()
A = readline()
B, C = readline()

answers = []
for i in A:
    cnt = 0
    if i == B:
        answers.append(1)
        continue
    rest = i - B
    cnt += 1
    if rest > 0:
        remain = rest % C
        if remain > 0:
            cnt += 1
        cnt += rest // C
    else:
        answers.append(cnt)
        continue
    answers.append(cnt)

print(sum(answers))