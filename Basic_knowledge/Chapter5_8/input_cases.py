# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:42:26 2021

@author: lenovo
"""

#%% [1]10的整数倍
active = True
while active:
    number = input('Please enter a number: ')
    if number == 'quit':
        active = False
    else:
        if int(number)%10:
            print('This number is not the multiple of 10.')
        else:
            print('This number is the multiple of 10.')

#%% [2]梦想的度假胜地
places = {}
polling_active = True
while polling_active:
    name = input('What is your name? ')
    place = input('Where would you visit? ')
    places[name] = place
    repeat = input('Anyone else to answer these questions? (yes/no) ')
    if repeat == 'no':
        polling_active = False
