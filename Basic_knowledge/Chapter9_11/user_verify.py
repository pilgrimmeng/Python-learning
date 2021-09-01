# -*- coding: utf-8 -*-
"""
验证用户

Created on Wed Sep  1 17:49:22 2021

@author: Meng Qiangfan
"""

import json


def get_stored_usernames(filename):
    '''尝试打开文件获取用户名列表'''
    try:
        with open(filename) as f:
            usernames = json.load(f)
    except FileNotFoundError:
        print('You are our first user!')
        return None
    else:
        return usernames

def store_username(filename, usernames, username):
    usernames.append(username)
    with open(filename, 'w') as f:
        json.dump(usernames, f)
    print(f'We will remember you when you come back, {username.title()}!')

def get_new_username(filename):
    '''提示新用户输入用户名'''
    username = input('Please enter your name: ')
    usernames = get_stored_usernames(filename)
    if usernames:
        if username.lower() in usernames:
            print(f'Welcome back, {username.title()}!')
        else:
            store_username(filename, usernames, username.lower())
    else:
        usernames = []
        store_username(filename, usernames, username.lower())