# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:01:52 2021

@author: lenovo
"""
#%% [1]个性化消息
name = "meng qiangfan"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

#%% [2]调整名字的大小写
first_name = "meng"
last_name = "qiangfan"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

#%% [3]名言
famous_people = 'Albert Einstein'
quote = '“A person who never made amistake never tried anything new.”'
motto = f'{famous_people} once said, {quote}'
print(motto)

#%% [4]剔除人名中的空白
name = "\t Xu Minpeng\n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())