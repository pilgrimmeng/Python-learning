# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:27:49 2021

@author: lenovo
"""

#%% [1]城市
def describe_city(city, country='China'):
    '''打印城市及所属国家'''
    print(f'{city} is in {country}.')

describe_city('Taiwan')
describe_city('Xianggang')
describe_city('London', 'the United Kingdom')

#%% [2]发送消息
text_messages = ['hello', 'congratulations', 'good morning']

def show_messages(messages):
    while messages:
        message = messages.pop()    #从结果来看是从末尾开始弹出
        print(f'{message.title()}!')

def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop()
        print(f'{message.title()}!')
        sent_messages.append(message)
    return sent_messages

#调用第一个函数时应该先创建一个副本
messages_copy = text_messages[:]
show_messages(messages_copy)

#调用第二个函数可以得到新的列表
sent_messages = send_messages(text_messages)

#%% [3]汽车
def make_car(manu, model, **car_info):
    car_info['manufacturer'] = manu
    car_info['model'] = model
    return car_info

car = make_car('Hongqi', 'H9+', color='blue', tow_package=True, price=50_0000)
print(car)
