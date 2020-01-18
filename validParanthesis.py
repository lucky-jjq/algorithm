'''
Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

def valid_param(s):
    los = list(s)
    param_set = {')':'(',  '}':'{', ']':'['}
    temp = []
    
    for c in los:
        print c
        if c not in param_set:
            temp.append(c)
        else:
            if temp[-1] != param_set[c]:
                return "invalid pair"
            else:
                temp.pop(-1)
    return "valid pair"
    

valid_param("()[]{}")
