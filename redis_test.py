#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='127.0.0.1', port=6379, db=0, password='123456')
redis_template = StrictRedis(connection_pool=pool)


def test_string():
    redis_template.set("wang", "wangzhiqiang")
    print(redis_template.exists("wang"))  # 判断一个key是否存在
    print(redis_template.get("wang"))  # 获取key的值
    print(redis_template.type("wang"))  # 判断key的类型
    print(redis_template.keys("wan*"))  # 按照pattern来获取key集合，慎用
    print(redis_template.rename("wang", "wang"))  # 重命名key
    redis_template.expire("wang", 60 * 60)  # 设置key的过期时间
    print(redis_template.ttl("wang"))  # 获取key的过期时间
    # flushdb() 删除当前选择数据库中的所有键
    # flushall()删除所有数据库中的所有键


def test_list():
    redis_template.rpush("user", "wangzhiqiang1")
    redis_template.rpush("user", "wangzhiqiang2")
    redis_template.rpush("user", "wangzhiqiang3")
    print(redis_template.llen("user"))
    # print(redis_template.lrange("user", 1, 2))
    # print(redis_template.lindex("user", 1))
    # print(redis_template.rpop("user"))
    # print(redis_template.rpop("user"))
    # print(redis_template.rpop("user"))
    # print(redis_template.delete("user"))


def test_hash():
    redis_template.hset('user', "name", "wang")
    redis_template.hset("user", "age", 25)
    redis_template.hset("user", "price", 25999999.9)
    #redis_template.hmset('user', mapping={'email': '130@163.com', 'score': '100'})
    #print(redis_template.hmget("user", ['email', 'score', 'price']))


if __name__ == '__main__':
    test_hash()
