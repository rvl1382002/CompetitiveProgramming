# Author: Riddhish V. Lichade

'''The goal of the game is to find where all the mines are located within a M × N field.
The game shows a number in a square which tells you how many mines there are adjacent to that square. Each square has at most eight
adjacent squares. The 4×4 field on the left contains two mines, each represented by a “*” character.'''


from sys import stdin
def instr(): return stdin.readline().strip()
def inspsint(): return map(int, stdin.readline().strip().split())
count=0
while True:
    try:
        n, m = inspsint()
        count+=1
    except:
        break
    l=[]
    for _ in range(n):
        l.append(instr())
    if n+m<=0:
        continue
    print("Field #"+str(count)+":")
    ans=[]
    for i in range(n):
        row=""
        for j in range(m):
            if l[i][j]=='*':
                row+='*'
                continue
            thisValue=0
            for k in range(max(0,i-1),min(n-1,i+1)+1):
                for o in range(max(0,j-1),min(m-1,j+1)+1):
                    if l[k][o]=='*':
                        thisValue+=1
            row+=str(thisValue)
        print(row)
    print()
