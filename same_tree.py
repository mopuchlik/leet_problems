# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

@author: User
"""

# for a list but they have a class for this, see below
def same_tree(p, q):
    
    if len(p) != len(q):
        return False
    else:
        result = True
        for i in range(len(p)):
            if p[i] == q[i]:
                continue
            else: return False 
                
    return result

p = [1,2,1]
q = [1,1,2]

print(same_tree(p, q))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
#         if p == None and q == None: return True
#         if p == None or q == None: return False
        
#         result = p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
 
#         return result




