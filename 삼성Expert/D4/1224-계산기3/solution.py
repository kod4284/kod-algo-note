read = lambda: int(input())
readline = lambda: input().strip()

def solve():
    global st, stack
    n = read()
    line = readline()
    stack = []
    st = ""
    is_paren = False
    for i in line:
        if "0" <= i <= "9":
            st += i
        else:
            if i == "(":
                stack.append(i)
            elif i == ")":
                while stack:
                    p = stack.pop()
                    if p == "(":
                        break
                    st += p
            else:
                while stack:
                    lastv = stack[len(stack) - 1]
                    if lastv != "(" and lastv <= i:
                        p = stack.pop()
                        st += p
                    else:
                        break
                stack.append(i)
    while stack:
        p = stack.pop()
        st += p
    
    for i in st:
        if "0" <= i <= "9":
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                stack.append(a + b)
            else:
                stack.append(a * b)
    return stack[0]

for i in range(1, 11):
    print("#{} {}".format(i, solve()))