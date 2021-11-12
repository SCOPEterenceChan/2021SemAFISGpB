'''
Created on Nov 9, 2021

@author: tchan

Lab4 Part3 Q2

1. prompt user to enter three numbers a, b, c

2. if a > b and b > c:
   then largest = a
   else if b > a and a > c:
        then largest = b
        else if c > b and b > a:
             then largest = c
   
3. output / write / print / echo largest

test cases:

1,2,3
1,3,2
2,1,3
2,3,1
3,2,1
3,1,2
'''

a = int(input('enter number a :'))
b = int(input('enter number b :'))
c = int(input('enter number c :'))

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > b and c > a:
    largest = c 

print("largest number is: ", largest)

