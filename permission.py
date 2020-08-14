#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

from sqlalchemy import Column, String, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class Permission(Base):
    __tablename__ = 'choice_base_customer_mapping'

    id = Column(String(50), primary_key=True)
    unique_id = Column(String(50))
    last_update_time = Column(DateTime)


engine = create_engine('mysql+mysqlconnector://grouptwo:grouptwo123@172.31.231.195:3306/db_ccs')
DBSession = sessionmaker(bind=engine)
