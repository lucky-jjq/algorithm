'''
fibonacci
'''

def fibonacci(n):
    l = [i for i in range(n+1)]
    if n < 2:
        return l[n]
    for i in xrange(2,n+1):  
        l[i] = l[i-1] + l[i-2]
        print l
    return l[n]

def fibonacci2(n):
    import numpy as np
    if n == 0: return 0
    a = [[1,1],[1,0]]
    b = [[1,1],[1,0]]
    for i in range(n+1-3):
        a = np.dot(a,b)
        print a
    return a[0][0]

fibonacci2(6)
