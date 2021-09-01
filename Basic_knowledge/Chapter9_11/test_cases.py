# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:15:13 2021

@author: lenovo
"""

#%% [1]城市和国家
# def city_country(city, country, population):
#     information = f'{city.title()}, {country.title()}-population {population}'
#     return information

# import unittest

# class CityTestCase(unittest.TestCase):
#     '''测试函数city_country'''
#     def test_city_country(self):
#         '''能正确处理santiago chile 5000000这样的输出'''
#         information = city_country('santiago', 'chile', 5000000)
#         self.assertEqual(information, 'Santiago, Chile-population 5000000')

# if __name__ == '__main__':
#     unittest.main()

#%% [2]雇员
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.name = f'{first_name.title()} {last_name.title()}'
        self.salary = salary
    def give_raise(self, increasement=5000):
        self.salary += increasement

import unittest

class EmployeeTestCase(unittest.TestCase):
    '''测试类Employee'''
    def setUp(self):
        '''创建一个雇员对象，生成一个年薪增加量'''
        self.my_employee = Employee('liu', 'bei', 10000)
        self.increment = 10000
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 15000)
    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 20000)

if __name__ == '__main__':
    unittest.main()