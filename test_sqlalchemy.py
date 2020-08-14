#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

from permission import DBSession
from permission import Permission

session = DBSession()
mapping = session.query(Permission).filter(Permission.id == '100000000001725275').one()

print(mapping.id)
print(mapping.unique_id)
print(mapping.last_update_time)
session.close()
