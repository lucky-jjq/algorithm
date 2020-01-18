'''
448. Find All Numbers Disappeared in an Array
'''
nums = [4,3,2,7,8,2,3,1]

def allNumMissing(nums):
  return list(set(range(1, len(nums) + 1)).difference(set(nums)))
