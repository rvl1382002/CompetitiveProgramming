# Author: Riddhish V. Lichade
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
**s consists of parentheses only '()[]{}'.'''

stack= []
s = input()
for i in s:
    if i in '({[':
        stack.append(i)
    else:
        if i == '}':
            lastElement=stack.pop()
            if lastElement!='{':
                print("False")
                exit()
        elif i == ')':
            lastElement=stack.pop()
            if lastElement!='(':
                print("False")
                exit()
        elif i == ']':
            lastElement = stack.pop()
            if lastElement != '[':
                print("False")
                exit()
if len(stack)==0:
    print("True")
else:
    print("False")