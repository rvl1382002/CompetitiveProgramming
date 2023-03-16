# Author: Riddhish V. Lichade

'''Consider the following algorithm to generate a sequence of numbers. Start with an integer n. If n is even, divide by 2. If n is odd,
 multiply by 3 and add 1. Repeat this process with the new value of n, terminating when n=1.
  It is conjectured that this algorithm will terminate at n=1 for every integer n. Still the conjecture holds true for all integers up
  to atleast 1,000,000.
  For an input n, the cycle length of n is the number of numbers generated up to and including the 1. Given any two numbers i and j, you
  are to determine the maximum cycle length over all numbers between i and j including both endpoints. '''

''' o/p format: For each pair of input integers i and j, output i,j in the same order in which they appeared in the input and then the 
 maximum cycle length for integers between and including i and j. These 3 numbers should be separated by one space, with all three number 
 on one line of output for each line of input'''

from sys import stdin

def inspsint(): return map(int, stdin.readline().strip().split())


dp = {1: 1, 2: 2}
while True:
    try:
        i, j = inspsint()
    except:
        break
    maxCycleLength = -1
    for k in range(i, j + 1):
        if k not in dp:
            l = k
            count = 1
            while l != 1:
                if l % 2 == 0:
                    l //= 2
                else:
                    l = l * 3 + 1
                if l in dp:
                    count+=dp[l]
                    break
                else:
                    count+=1
            dp[k] = count
        maxCycleLength = max(maxCycleLength, dp[k])
    print(i,j,maxCycleLength)

