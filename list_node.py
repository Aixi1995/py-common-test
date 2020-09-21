#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'


class ListNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

    def __str__(self):
        if self is None:
            return 'None'
        return str(self.elem) + '-' + self.next.__str__()


# 循环方式反转链表
def reverse(head):
    pre = None
    while head:
        next_ = head.next
        head.next = pre
        pre = head
        head = next_
    return pre


if __name__ == '__main__':
    node4 = ListNode(4, next_=None)
    node3 = ListNode(3, next_=node4)
    node2 = ListNode(2, next_=node3)
    node1 = ListNode(1, next_=node2)
    print(node1.__str__())
    reverse_node = reverse(node1)
    print(reverse_node.__str__())
