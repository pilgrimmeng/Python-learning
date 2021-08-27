# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:59:10 2021

@author: lenovo
"""
#%% [1]姓名
names = ['zhang liao', 'xu huang', 'zhang he', 'yue jin', 'yu jin']
for x in names:
    print(f'{x.title()}')

#%% [2]问候
for x in names:
    print(f'Hello, {x.title()}!')

#%% [3]邀请
for x in names:
    print(f'Hello, {x.title()}! Would you like to have dinner with me?')

#%% [4]修改
name_absent = 'yu jin'      #缺席嘉宾
name_add = 'xu chu'         #新的嘉宾
names.remove(name_absent)
names.append(name_add)
print(f'Sorry to hear that {name_absent.title()} can not come here.\n\
I would like to invite {name_add.title()} for our dinner.')
for x in names:
    print(f'Hello, {x.title()}! Would you like to have dinner with me?')

#%% [5]添加
names_add = ['dian wei', 'guojia', 'li dian']
print(f'I have found a bigger table.')
names.insert(0, names_add[1])
names.insert(3, names_add[0])
names.append(names_add[2])
for x in names:
    print(f'Hello, {x.title()}! Would you like to have dinner with me?')

#%% [6]缩减
print(f'Sorry to hear that the big table can not be sent here in time.')
num_max = 2     #最后只剩2个人
for i in range(num_max, len(names)):    #一直删最后一个人
    del names[-1]

#%% [7]排序
generals = ['zhang liao', 'xu huang', 'zhang he', 'yue jin', 'yu jin']
print(generals)                         #按原始排列顺序打印
print(sorted(generals))                 #按字母顺序打印
print(generals)                         #核实排列顺序未变
print(sorted(generals, reverse=True))   #按与字母顺序相反的顺序打印
print(generals)                         #核实排列顺序未变
generals.reverse()
print(generals)                         #修改列表元素的排列顺序
generals.reverse()
print(generals)                         #核实已恢复到原来的排列顺序
generals.sort()
print(generals)                         #按字母顺序排列
generals.sort(reverse=True)
print(generals)                         #按与字母顺序相反的顺序打印
print(f'There are {len(generals)} generals.')