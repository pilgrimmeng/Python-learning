# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 18:10:49 2021

@author: lenovo
"""
#%% [1]列表解析
#一百万求和
numbers = [value for value in range(1,1000000+1)]
min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
#立方
num_cube = [value**3 for value in range(1,11)]
#num_slice = num_cube[0:9:2]     #从索引0到8（9-1），距离2取一个，即0,2,4,6,8

#%% [2]切片
generals = ['zhang liao', 'xu huang', 'zhang he', 'yue jin', 'yu jin']
gene_sort = sorted(generals)
print(gene_sort)
print(f'The first three items in this list are: {gene_sort[:3]}')
print(f'The middle three items in this list are: {gene_sort[1:4]}')
print(f'The last three items in this list are: {gene_sort[-3:]}')
gene_new = gene_sort[:]
gene_new.append('dian wei')
print(gene_new)

#%% [3]元组
gene_5 = ('zhang liao', 'xu huang', 'zhang he', 'yue jin', 'yu jin')
# gene_5[3] = 'dian wei'