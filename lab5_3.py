#!/usr/bin/env python3
import sys
import math
import random

#Intro

print ('\n Guten tag! Let`s play "Rock, Paper, Scissors" ')
print ('''The conditions of da game: 

number 1 is the ROCK
number 2 is da PAPER
number 3 is de SCISSORS

Game is started!!! :)
''')

#User

user = int(input('input your number: '))

if user == 1:
    print('You choosed the ROCK ')
elif user == 2:
    print('You choosed da PAPER ')
elif user == 3:
    print('You choosed de SCISSORS ')
else:
    print('Wrong number')

#Computer

comp = random.randint(1,3)

if comp == 1:
    print('Comp choosed the ROCK ')
elif comp == 2:
    print('Comp choosed da PAPER ')
elif comp  == 3:
    print('Comp choosed de SCISSORS ')

#logic the program

if comp == user:
    print('Draw! ')
elif ((user == 2 and comp == 3)
or (user == 3 and comp == 1)
or (user == 1 and comp == 2)):
    print('Comp wins ')
else:
    print('You win ')

