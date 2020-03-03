# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

import math
def solution(s):
    #returns empty list if empty string is passed in
    if len(s) == 0:
        return []
    l = []
    for i in range(len(s)):
        # appends character if the index is even
        if i % 2 == 0:
           l.append(s[i])
        # else appends the next character in the sequence
        else:
            l[math.floor((i-1)/2)] += s[i] 
    # adds underscore to last element if the length of the last element is equal to 1   
    if len(l[-1]) == 1:
        l[-1] += '_'
    return l