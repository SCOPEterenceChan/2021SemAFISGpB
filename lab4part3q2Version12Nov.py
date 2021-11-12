'''
Created on Nov 9, 2021

@author: tchan

Lab4 Part3 Q2

1. prompt user to enter three numbers

2. largest = max(a,b,c)

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

largest = max(a,b,c)

print("largest number is: ", largest)

