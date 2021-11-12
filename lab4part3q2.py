'''
Created on Nov 9, 2021

@author: tchan

Lab4 Part3 Q2

1. input / get / read three numbers a,b,c

2. largest = a

   if b > largest
   then largest = b

   if c > largest
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
a,b,c = 1,2,3
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("largest number is: ", largest)

