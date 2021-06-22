# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
data={1:'raj',2:'kiran',4:'ram'}

data.copy()
print(data)

y=data.fromkeys(data)
print(y)

x=data.get(1)
print(x)

x=data.items()
print(x)

z=data.keys()
print(z)

data.pop(1)
print(data)

data.popitem()
print(data)

data.setdefault(3)
print(data)

data.update({'5':'rahul'})
print(data)

data.clear()
print(data)

data.values()
print(data)

