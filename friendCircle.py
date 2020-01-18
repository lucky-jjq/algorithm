'''
547. Friend Circles
1st method: dfs
'''

grid = [[1,1,1],
        [1,1,0],
        [1,0,1]]

def findCircleNum(M):
    all_friends = []
    n = len(M)
    ans = 0
    for i in xrange(n):
        print ans
        if M[i][i]: 
            ans += 1
        cnt_friends = dfs(i,n,M) # find all friends
    return ans
            
def dfs(i,n,M):
    for j in xrange(n):
        if M[i][j] == 0:
            continue 
        else:
            M[i][j] = 0
            M[j][i] = 0
            cnt = dfs(j,n,M)
            print M

findCircleNum(grid)
