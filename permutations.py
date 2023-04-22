# Author: Riddhish V. Lichade

'''Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''

from itertools import permutations
l=eval(input())
ans=permutations(l)
ans=list(ans)
# print(ans)

#Without using in-built function using recursion
def permutation(l):
    if len(l)==0:
        return []
    if len(l)==1:
        return l
    ans=[]
    for i in range(len(l)):
        thisElement=[l[i]]
        remainingList = l[:i] + l[i+1:]
        for j in permutation(remainingList):
            # print(thisElement,"   j=",j,"         ",thisElement+[j])
            ans.append(thisElement+[j])
    return ans
ans = permutation(l)
print(ans)