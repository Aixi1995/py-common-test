#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

import json

from elasticsearch import Elasticsearch
from es_common_api import es, close_es


match_all = {"query": {"match_all": {}}}
term_query = {
    "query": {
        "term": {
            "customer_id": 38
        }
    },
    "_source": {
        "includes": ["category", "currency", "customer_id"]
    }
}

# 组合查询
multi_search = ('{"index":"kibana_sample_data_ecommerce"} ',
                '{"query" : {"term" : {"customer_id": 38}}} ',
                '{"index":"kibana_sample_data_ecommerce"} ',
                '{"query" : {"term" : {"customer_id": 37}}} ',
                '{"index":"kibana_sample_data_ecommerce"} ',
                '{"query" : {"match" : {"currency": "EUR"}}} ')


def search(query_body, size):
    return es.search(index='kibana_sample_data_ecommerce', body=query_body, size=size)['hits']['hits']


# UMt7N3MBxwpYwKrrU2zf
def search_by_id(_id):
    return es.get(index='kibana_sample_data_ecommerce', id=_id, _source='customer_id')['_source']


def msearch(body):
    return es.msearch(body=body)


if __name__ == '__main__':
    print(msearch(multi_search))
    # print(search(term_query, 2))
