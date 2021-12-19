import math, bisect
readline = lambda: list(map(int, input().split()))

class Node:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
        self.cnt = 0
    def up_count():
        self.cnt += 1

def init(node, number, goal):
    global root
    if number == 1:
        root = node
    if number >= goal:
        return
    node.left = Node()
    node.right = Node()
    init(node.left, number * 2, goal)
    init(node.right, (number * 2) + 1, goal)

if __name__ == '__main__':
    n, m = readline()
    a = readline()
    set_a = set()
    total = 2**math.ceil(math.log2(n))
    root = Node()
    # tree = [[] fr _ in range()]
    q = []
    for _ in range(m):
        i, j, k = readline()
        q.append((i, j, k))
    a.sort()
    for i in a:
        set_a.add(i)
    list_a = list(set_a)
    # a: 
    # set_a:
    # list_a: 

    tmp = init(Node(), 1, 8)
    print(root.left)
