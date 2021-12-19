def operate(a, b, op):
    if op == "+":
        return int(a) + int(b)
    elif op == "*":
        return int(a) * int(b)

def solve():
    stack = []
    postfix = ""
    l = int(input())
    st = input()
    for i in st:
        if "0" <= i and i <= "9":
            postfix += i
        else:
            while stack:
                op = stack.pop()
                if op <= i:
                    postfix += op
                else:
                    stack.append(op)
                    break
            stack.append(i)
    while stack:
        op = stack.pop()
        postfix += op
    
    for i in postfix:
        if "0" <= i and i <= "9":
            stack.append(i) 
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(operate(a, b, i))
    return stack.pop()

TC = 10
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))