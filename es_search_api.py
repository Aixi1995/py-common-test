#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

from elasticsearch import Elasticsearch
from es_common_api import es, close_es

match_all = {"query": {"match_all": {}}}
term_query = {
    "query": {
        "term": {
            "customer_id": 38
        }
    }
}


def search(query_body, size):
    return es.search(index='kibana_sample_data_ecommerce', body=query_body, size=size)['hits']['hits']


def search_by_id(_id):
    return es.get(index='kibana_sample_data_ecommerce', id=_id)['_source']  # UMt7N3MBxwpYwKrrU2zf


if __name__ == '__main__':
    print(search_by_id('UMt7N3MBxwpYwKrrU2zf'))
    print(search(term_query, 2))
