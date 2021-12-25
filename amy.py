#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    a=bin(n).replace("0b","")
    a1=str(a)
    l=len(a1)
    s='0'*(32-l)
    s=s+a1
    mylist=[]
    for ch in s:
        if ch=='0':
             mylist.append('1')
        else:
            mylist.append('0')
    mystr=''
    for ii in mylist:
        mystr = mystr + ii
    myint= int(mystr)
    decimal=0
    i=0
    while (myint != 0):
        dec=myint%10
        decimal = decimal +dec * pow(2,i)
        myint=myint//10
        i=i+1
    return decimal
        
        
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
