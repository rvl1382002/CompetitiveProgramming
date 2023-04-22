# Author: Riddhish V. Lichade
# username: root_rvl
#This program is not complete yet
#doing minus its going in negative indexing... correct it

from collections import Counter, defaultdict
from sys import stdin, stdout, setrecursionlimit
from heapq import nlargest, nsmallest
import math

def instr(): return stdin.readline().strip()
def inlist(): return list(map(int, stdin.readline().strip().split()))
#small cases : Black
#capital case: White
totalDots=1
while totalDots<64:
    l=[]
    totalDots=0
    # Taking Input
    for _ in range(8):
        s=instr()
        totalDots+=s.count('.')
        if 'k' in s:
            ki=_
            kj=s.index('k')
        if 'K' in s:
            Ki=_
            Kj=s.index('K')
        l.append(s)
    if totalDots==64:
        break
    #-----------------------------------------------------------------------------------------
    #Checking if black king has a check

    #Check check from pawns
    try:
        if l[ki-1][kj-1] == 'P' or l[ki+1][kj-1]=='P':
            print("black king is in check")
            print("pawn")
            continue
    except:
        pass

    #Check check from knight
    try:
        if l[ki-1][kj+2]=='N' or l[ki-1][j-2]=='N' or l[i+1][kj-2]=='N' or l[ki+1][kj+2]=='N' or l[ki-2][kj+1]=='N' or l[ki-2][kj-1]=='N'\
            or l[ki+2][kj-1]=='N' or l[ki+2][kj+1]=='N':
            print("black king is in check")
            print("knight")
            continue
    except:
        pass

    #Check check from rook or queen horizontal or vertical
    #checking above king
    try:
        # checking above king
        check=False
        for j in range(kj+1,8):
            if l[ki][j] != '.':
                if l[ki][j] in 'RQ':
                    check=True
                break
        if check:
            print("black king is in check")
            print("Rook up")
            continue
    except:
        pass

    # checking below king
    try:
        for j in range(kj-1, -1,-1):
            if l[ki][j] != '.':
                if l[ki][j] in 'RQ':
                    check = True
                break
        if check:
            print("black king is in check")
            print("Rook down")
            continue
    except:
        pass

    #checking horizontal left from king
    try:
        for i in range(i-1,-1,-1):
            if l[i][kj]!='.':
                if l[i][kj] in 'RQ':
                    check=True
                break
        if check:
            print("black king is in check")
            print("Rook left")
            continue
    except:
        pass

    # checking horizontal right from the king
    try:
        for i in range(i + 1, 8):
            if l[i][kj] != '.':
                if l[i][kj] in 'RQ':
                    check = True
                break
        if check:
            print("black king is in check")
            print("Rook right")
            continue
    except:
        pass

    # checking diagonals

    try:
        for i in range(1,8):
            if l[ki+i][kj+i] != '.':
                if l[ki+i][kj+i] in 'BQ':
                    check=True
                break
        if check:
            print('black king is in check')
            print("diagonal ++")
            continue
    except:
        pass

    #Next diaognal
    try:
        for i in range(1,8):
            if l[ki-i][kj-i] != '.':
                if l[ki-i][kj-i] in 'BQ':
                    check=True
                break
        if check:
            print('black king is in check')
            print("diagonal --")
            print(ki-i,kj-i)
            continue
    except:
        pass

    #next diagonal
    try:
        for i in range(1,8):
            if l[ki+i][kj-i] != '.':
                if l[ki+i][kj-i] in 'BQ':
                    check=True
                break
        if check:
            print('black king is in check')
            print("diagonal +-")
            continue
    except:
        pass

    #next diagonal
    try:
        for i in range(1,8):
            if l[ki-i][kj+i] != '.':
                if l[ki-i][kj+i] in 'BQ':
                    check=True
                break
        if check:
            print('black king is in check')
            print("diagonal -+")
            continue
    except:
        pass

#-------------------------------------Checking if white king is in check---------------------------------

