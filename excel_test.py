#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

import xlrd
import xlwt
import re

workbook_path = r'd:\2020.07-24制造.xls'
workbook_des_path = r'd:\处理后.xlsx'
l = []


def need_del(phone):
    res = re.search(r'^1[3456789]\d{9}$', str(phone))
    return res is None


def clean(cols_phones):
    for phone in cols_phones:
        phone_str = str(phone)
        if ' ' in phone_str:
            for p in phone_str.split(' '):
                if not need_del(p):
                    l.append(p)
        else:
            if not need_del(phone_str):
                l.append(phone_str)


def write2excel(l1, sheet):
    for row in range(l1.__len__()):
        sheet.write(row, 0, l1[row])


if __name__ == '__main__':
    workbook = xlrd.open_workbook(workbook_path)
    sheet = workbook.sheet_by_index(0)
    cols_phones = sheet.col_values(0)
    clean(cols_phones)
    workbook_des = xlwt.Workbook()
    sheet_des = workbook_des.add_sheet("after handle")
    write2excel(l, sheet_des)
    workbook_des.save('d:\\1.xlsx')
