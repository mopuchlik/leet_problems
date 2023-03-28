#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:41:39 2023

https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

@author: michal
"""

# Definition for singly-linked list.

# %%


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# %%


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val = carry
        if [l1.val] != None:
            val += l1.val
            l1 = ListNode(l1.next)
        if [l2.val] != None:
            val += l2.val
            l2 = ListNode(l2.next)
        carry, val = divmod(val, 10)
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# %%
l1 = ListNode()
l2 = ListNode()

l1.val = 2
l1.next = 4

l2.val = 5
l2.next = 6

addTwoNumbers(l1, l2)

# %% linked list representation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()
first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node
llist
