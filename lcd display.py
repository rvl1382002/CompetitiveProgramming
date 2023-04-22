# Author: Riddhish V. Lichade
# username: root_rvl
'''
A friend of yours has just bought a new computer. Before this, the most powerful
machine he ever used was a pocket calculator. He is a little disappointed because he
liked the LCD display of his calculator more than the screen on his new computer! To
make him happy, write a program that prints numbers in LCD display style.
'''

from sys import stdin

def inspsint(): return map(str, stdin.readline().strip().split())

def Line1(n,number):
    if number in "02356789":
        print(" "+"_"*n+" ",end=" ")
    else:
        print(" "*(n+2),end=" ")

def Line2(n,number):
    if number in "56":
        print("|"+" "*(n+1),end=" ")
    elif number in "1237":
        print(" "*(n+1)+"|",end=" ")
    else:
        print("|"+" "*n+"|",end=" ")

def Line3(n,number):
    if number in "2345689":
        print(" "+"_"*n+" ",end=" ")
    else:
        print(" "*(n+2),end=" ")

def Line4(n,number):
    if number == '2':
        print("|"+" "*(n+1),end=" ")
    elif number in "134579":
        print(" "*(n+1)+"|",end=" ")
    else:
        print("|"+" "*n+"|",end=" ")

def Line5(n,number):
    if number in "0235689":
        print(" "+"_"*n+" ",end=" ")
    else:
        print(" "*(n+2),end=" ")


if __name__=='__main__':
    n,number = inspsint()
    n=int(n)
    for i in str(number):
        Line1(n,i)
    print()
    for _ in range(n):
        for i in str(number):
            Line2(n,i)
        print()
    for i in str(number):
        Line3(n,i)
    print()
    for _ in range(n):
        for i in str(number):
            Line4(n,i)
        print()
    for i in str(number):
        Line5(n,i)
