#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zq'

from elasticsearch import Elasticsearch

es = Elasticsearch([
    'localhost:9200'
])


def close_es():
    """关闭es client链接"""
    es.close()


def get_health():
    """获取es的健康状态"""
    return es.cluster.health()['status']


def get_indices(index):
    """获取索引信息"""
    return es.cat.indices(index=index)


def refresh_index(index):
    """索引的刷新"""
    es.indices.refresh(index=index)


if __name__ == '__main__':
    print('es cluster health is : %s' % get_indices('kibana_sample_data_ecommerce'))
    close_es()
