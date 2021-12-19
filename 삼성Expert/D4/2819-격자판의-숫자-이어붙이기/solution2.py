directions = [(-1,0), (1, 0), (0,-1), (0,1)]

def helper(r, c, count, lst, num):
    if count == 7:
        return [num]
    else:
        for dr, dc in directions:
            if  (dr+r>3) or (dr+r<0) or (dc+c>3) or (dc+c<0):
                continue
            lst.add(helper(r+dr, c+dc, count+1, lst, num*10 + int(board[r+dr][c+dc])))
        return lst


T = int(input().strip())
board = []
final_list=set()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    for i in range(4):
        board.append(input().strip().split(" "))
    
    for r in range (len(board)):
        for c in range (len(board[0])):
            final_list = helper(r, c, 1, final_list, int(board[r][c]))
   
    print("#{0} {1}".format(test_case, len(set(final_list))))