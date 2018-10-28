#!/usr/bin/env python3
import sys
import math

print('Quadratic equation is: ax^2 + bx +c = 0')
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

print('Your equation is: ',a,'x^2 +',b,'x +',c,'= 0')


D = math.pow(b,2) - 4*a*c

#if D>0:
x1 = (-b - math.sqrt(D)) / (2*a)
x2 = (-b + math.sqrt(D)) / (2*a)

#elif D==0:
x1 = -b / (2*a)
x2 = x1

print('The roots of da equation:', x1, x2)
