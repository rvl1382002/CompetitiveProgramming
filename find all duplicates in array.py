# Author: Riddhish V. Lichade
'''Given an integer array nums of length n where all the integers of nums are in the range [1,
n] and each integer appears once or twice, return an array of all the integers that
appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.'''
from collections import Counter
d = Counter(eval(input()))
ans=[]
for i in d:
    if d[i]==2:
        ans.append(i)
print(ans)