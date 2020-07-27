#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'


def calc(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


# 可变参数的形式定义函数
def _calc(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


print(calc([1, 2, 3, 4]))
print(_calc(1, 2, 3, 4))

# 将已经有的list或者tuple以可变参数传入
l = [1, 2, 3, 4]
print(_calc(*l))


def person(name, age, **kv):
    print('name:', name, 'age:', age, 'other:', kv)


person('wang', 25, city='shanghai')


def product(x, *y):
    if len(y):
        for i in y:
            x *= i
    return x


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
