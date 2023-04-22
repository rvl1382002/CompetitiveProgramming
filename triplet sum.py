# Author: Riddhish V. Lichade

'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''

l = eval(input())
l.sort()
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==0:
                m = [l[i],l[j],l[k]]
                if m not in ans:
                    ans.append(m)
print(ans)

#another logic
l.sort()
ans=[]
