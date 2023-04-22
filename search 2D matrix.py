# Author: Riddhish V. Lichade
'''Write an efficient algorithm that searches for a value target in an m x n integer
matrix matrix. This matrix has the following properties:
•Integers in each row are sorted from left to right.
•The first integer of each row is greater than the last integer of the previous row.
If value is present in given matrix return true else return false'''

# The 2-D list is sorted so we can simply convert it into a 1-D list and perform binary search

def binarySearch(a,target):
    l=0
    h=len(a)
    while l<=h:
        mid = (l+h)//2
        val=a[mid]
        if val==target:
            return True
        elif target < val:
            h=mid-1
        else:
            l=mid+1
    else:
        return False

if __name__ == '__main__':
    l=eval(input())
    target = int(input())
    combinedList = []
    for i in l:
        combinedList+=i
    print(binarySearch(combinedList,target))