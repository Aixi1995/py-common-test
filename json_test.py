#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

import json

data = {'name': 'Alex', 'company': 'Google', 'age': 34}

json_str = json.dumps(data)


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('wang', '25')

print(json.dumps(s, default=lambda obj: obj.__dict__))

s1 = json.load('{"name": "wang", "age": "25"}')
print(s1)
