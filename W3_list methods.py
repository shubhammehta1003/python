# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nums=[25,12,36,95,14,95]
values=[9.5,'Shubham',25]

nums.append(45)
print(nums)

nums.copy()
print(nums)

y=nums.count(95)
print(y)

nums.extend(values)
print(nums)

x=nums.index(14)
print(x)

nums.insert(1,"cat")
print(nums)

nums.pop(1)
print(nums)

nums.remove('Shubham')
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.clear()
print(nums)