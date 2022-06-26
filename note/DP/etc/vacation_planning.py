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

def printDP(dp):
    for i, row in enumerate(dp):
        print(row)
    print()
    

def vacPlan(S):
    n = len(S)
    dp = [[0] * n for _ in range(2)]

    def preorder(no):
        id = no - 1
        val = getVal(no)
        
        children = getChildren(no)
        if not children:
            dp[0][id] = 0
            dp[1][id] = val
        
        includeCurrSumMax = val
        excludeCurrSumMax = 0
        for c in children:
            preorder(c)
            idx = c - 1
            includeCurrSumMax += dp[0][idx]
            excludeCurrSumMax += max(dp[0][idx], dp[1][idx])
        printDP(dp)
        dp[0][id] = excludeCurrSumMax
        dp[1][id] = includeCurrSumMax
    
    preorder(1)
    printDP(dp)
    return max( dp[0][0], dp[1][0] )
    
print(vacPlan(S))