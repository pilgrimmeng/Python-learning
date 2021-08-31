# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:13:42 2021

@author: lenovo
"""

#%% [1]餐馆
class Restaurant:
    def __init__(self, name, res_type):
        self.name = name
        self.type = res_type
        self.number_served = 0
    def describe(self):
        print(f'This is a {self.type} restaurant named {self.name}.')
    def open_it(self, flag):
        if flag:
            print('This restaurant is open now.')
    def set_number_served(self, number):
        self.number_served = number
        print(f'This restaurant has served {self.number_served} customers.')
    def increment_number(self, number):
        self.number_served += number
        print(f'This restaurant served {number} customers today, and it has served {self.number_served} customers totally.')

my_res = Restaurant('Niufu', 'noodle')
my_res.describe()
my_res.open_it(True)
my_res.set_number_served(500)
my_res.increment_number(100)

#%% [2]冰激凌小店
class IceCreamStand(Restaurant):
    def __init__(self, name, res_type, flavors):
        super().__init__(name, res_type)
        self.flavors = flavors
    def show_list(self):
        print('This stand has these kinds of ice-cream:')
        for flavors in self.flavors:
            print(f'\t{flavors}')

my_stand = IceCreamStand('MiXueBingCheng', 'ice-cream', ['strawberry', 'paech', 'lemon'])
my_stand.describe()
my_stand.show_list()

#%% [3]彩票分析
from random import choice
ticket_select = list(range(10))+['a','b','c','d']
award_number = []
#抽出获奖号码
for seq in range(4):
    number = choice(ticket_select)
    award_number.append(number)
    ticket_select.remove(number)
#模拟抽奖
times = 0
if_award = 0
if_toomany = 0
flag = not (if_award or if_toomany)
while flag:
    times += 1
    my_ticket = []
    for seq in range(4):
        number = choice(ticket_select)
        my_ticket.append(number)
    if set(award_number) == set(my_ticket):
        if_award = 1
    elif times >= 1e6:
        if_toomany = 1
    flag = not (if_award or if_toomany)
