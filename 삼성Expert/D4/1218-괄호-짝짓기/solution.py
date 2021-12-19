
opening = ["[", "(", "{", "<"]
closing = ["]", ")", "}", ">"]

def solve():
    N = int(input())
    line = input()
    stack = []
    for i in line:
        if i in opening:
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            for idx in range(len(closing)):
                if i == closing[idx] and stack[len(stack) - 1] == opening[idx]:
                    stack.pop()
                    break
            else:
                return 0
    if len(stack) != 0:
        return 0
    return 1

for i in range(1, 11):
    print("#{} {}".format(i, solve()))