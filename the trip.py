# Author: Riddhish V. Lichade
'''
A group of students are members of a club that travels annually to different lo-
cations. Their destinations in the past have included Indianapolis, Phoenix, Nashville,

Philadelphia, San Jose, and Atlanta. This spring they are planning a trip to Eindhoven.
The group agrees in advance to share expenses equally, but it is not practical to share
every expense as it occurs. Thus individuals in the group pay for particular things, such
as meals, hotels, taxi rides, and plane tickets. After the trip, each student’s expenses
are tallied and money is exchanged so that the net cost to each is the same, to within
one cent. In the past, this money exchange has been tedious and time consuming. Your
job is to compute, from a list of expenses, the minimum amount of money that must
change hands in order to equalize (within one cent) all the students’ costs.
'''
# import math
def truncate(n,d=2):
    return int(n*10**d)/10**d
n=int(input())
while(n!=0):
    l=[]
    sum=0
    for i in range(n):
        val = float(input())
        l.append(val)
        sum+=val
    avg = truncate(sum/n)
    ans=0
    for i in l:
        if i<avg:
            ans+=round(truncate(avg-i),2)
    print(ans)
    n=int(input())