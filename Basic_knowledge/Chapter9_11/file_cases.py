# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:10:21 2021

@author: lenovo
"""

#%% [1]圆周率值中包含你的生日吗
filename = 'pi_million_digits.txt'
with open(filename) as file_pi:
    lines = file_pi.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in the form yymmdd: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digists of pi!')
else:
    print('Your birthday does not appear in the first million digists of pi.')

#%% [2]访客名单
flag = 1
filename = 'guest_book.txt'
while flag:
    name = input('Please enter your name: ')
    if name == 'quit':
        flag = 0
    else:
        print(f'Welcome, {name.title()}!')
        with open(filename, 'a') as file_guest:
            file_guest.write(f'{name.title()}\n')

#%% [3]常见单词
# import file_analyse
# from file_analyse import special_words_count
# from file_analyse import special_words_count as swc
# import file_analyse as fa
from file_analyse import *

txtnames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
file = 'books\\'
word_num = []
for txtname in txtnames:
    # word_num.append(file_analyse.special_words_count(file+txtname, 'the'))
    # word_num.append(special_words_count(file+txtname, 'the'))
    # word_num.append(swc(file+txtname, 'the'))
    # word_num.append(fa.special_words_count(file+txtname, 'the'))
    # word_num.append(words_count(file+txtname))
    word_num.append(special_words_count(file+txtname, 'the '))

#%% [4]验证用户
import user_verify as uv

filename = 'usernames.json'
uv.get_new_username(filename)
