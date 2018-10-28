#!/usr/bin/env python3
import sys
import math

#Enter the data
print('Input the sides (a,b,c) of triangle ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

#Program logic
if ((c>=a and c>=b and a+b>c)
or (b>=a and b>=c and a+c>b)
or (a>=b and a>=c and b+c>a)):
    print('Triangle has been exist')
elif (a == 0 or b == 0 or c == 0):
    print('''Triangle hasn't been exist''')
else:
    print('''Triangle hasn't been exist''')
