'''
two sum-easy
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def two_sum(lst, target):
    remain = {}
    for i, n in enumerate(lst):
        if n in remain.keys():
            return [remain[n], i]
        else:
            remain[target - lst[i]] = i
        print remain
    return None

two_sum([2, 11,7, 15], 9)
