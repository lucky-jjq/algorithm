'''
array - easy
485.Max Consecutive Ones 
Given a binary array, find the maximum number of consecutive 1s in this array.
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

'''

l = [1,1,0,1,1,1]

def max_consec(l):
    prev = l[0]
    cnt = 0
    ret = 0
    for n in l[1:]:
        if n == prev:
            cnt += 1
        else:
            cnt = 0
        if cnt > ret:
            ret = cnt
    return ret
max_consec(l)
