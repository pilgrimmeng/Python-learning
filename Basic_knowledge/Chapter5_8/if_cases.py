# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% [1]外星人颜色
colors = ['green', 'yellow', 'red']
for alien_color in sorted(colors):
    if alien_color == 'green':
        print('Congratulations! You got 5 points for this killing!')
    elif alien_color == 'yellow':
        print('Congratulations! You got 10 points for this killing!')
    elif alien_color == 'red':
        print('Congratulations! You got 15 points for this killing!')

#%% 检查用户名
current_users = ['Zhang liao', 'xu huang', 'zhang he', 'yue jin', 'yu jin']
#创建小写副本
current_users_lower = []
for index in range(0,len(current_users)):
    current_users_lower.append(current_users[index].lower())
new_users = ['lv bu', 'zhao yun', 'dian wei', 'Guan yu', 'zhang liao']

#判断用户名是否已存在
for user in new_users:
    if user.lower() in current_users_lower:
        print('Sorry, this user name is already in use. Please enter another user name!')
    elif user.lower() not in current_users_lower:
        print('This user name can be used.')