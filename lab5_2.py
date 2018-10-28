#!/usr/bin/env python3
import sys
import math

h = 2
w = 1

print('The size of da door is 1x2 \n')
print('Please, input da size of a box (a, b, c) in meters \n')
a = float(input('a =  '))
b = float(input('b =  '))
c = float(input('c =  '))

if ((a<h and b<h)
or (a<h and c<h)
or (b<h and c<h)

or (a<w and b<w)
or (a<w and c<w)
or (b<w and c<w)):
    print('Congratulation! You are an lifter')
else:
    print('You are a noob')
