from typing import List
S = [10, 6, 5, 2, 7, 4, 11]
CH = [ [2, 4], [3, 5, 6], [], [], [], [7], [] ]

def getRoot():
    return S[0]

def getNode(no):
    return S[no - 1]

def getChildren(no):
    # return list(map(lambda x: x - 1, S[no - 1][2]))
    return CH[no - 1]

def getVal(no):
    return S[no - 1]

def vacPlan(S):
    n = len(S)
    dp = [[0] * n for _ in range(2)]

    def preorder(no):
        id = no - 1
        val = getVal(no)
        children = getChildren(id)
        include
        for c in children:

        
    
    preorder(1)


    return 
    
print(vacPlan(S))