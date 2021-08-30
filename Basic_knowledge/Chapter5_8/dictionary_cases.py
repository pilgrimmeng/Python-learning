# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:40:24 2021

@author: lenovo
"""

#%% [1]词汇表
vocabulary = {
    '变量': '指向一个值——与该变量相关联的信息，在程序中可随时修改',
    '列表': '列表由一系列按特定顺序排列的元素组成',
    '常量': '其值在程序的整个生命周期内保持不变',
    '列表解析': '将for循环和创建新元素的代码合并成一行，并自动附加新元素',
    '条件测试': '每条if语句的核心都是一个值为True或False的表达式，这种表达式称为条件测试',
    }
for word in vocabulary:
    print(f'{word}： {vocabulary.get(word)}')

#%% [2]调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
people_survey = ['jen', 'bob', 'edward']
for person in people_survey:
    if person in favorite_languages.keys():
        print(f'Thanks for your cooperation, {person.title()}!')
    else:
        print(f'Would you like to participate in our survey about your favorite language, {person.title()}?')

#%% [3]嵌套
majesty = {
    'cao cao': ['zhang liao', 'dian wei', 'xu chu'],
    'sun quan': ['zhou yu', 'lu xun', 'lv meng'],
    'liu bei': ['guan yu', 'zhang fei', 'zhao yun'],
    }
for master in majesty:
    general_names = '';
    for general in majesty[master]:
        general_names = general_names + f'{general.title()}, '
    print(f'The majesty {master.title()} has some famous generals such as {general_names}and so on.')
    del general_names