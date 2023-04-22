# Author: Riddhish V. Lichade
'''Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value.
If target is not found in the array, return [-1, -1].'''

l=eval(input())
target = int(input())
try:
    x=y=l.index(target)
except:
    print([-1,-1])
    exit()
for i in range(x+1,len(l)):
    if l[i]!=target:
        y=i-1
print([x,y])