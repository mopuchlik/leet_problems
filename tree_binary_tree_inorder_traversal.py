# https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line/


#### IDEA ############

### Graph is like this
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6


# Inorder (Left → Root → Right) --> Down->Top
# Output: [4, 2, 5, 1, 3, 6]

# Preorder (Root → Left → Right) --> Top-Down
# Output: [1, 2, 4, 5, 3, 6]

# Postorder (Left → Right → Root) --> Down->Top
# Output: [4, 5, 2, 6, 3, 1]

# BFS / Level-order (Top-down, left-to-right)
# Output: [1, 2, 3, 4, 5, 6]

from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# (Left → Root → Right) Down->Top
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def traverse(current_node):
        if not current_node:
            return
        traverse(current_node.left)
        result.append(current_node.val)
        traverse(current_node.right)

    traverse(root)
    return result


# (Root → Left → Right) --> Top->Down
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def traverse(current_node):
        if not current_node:
            return
        result.append(current_node.val)
        traverse(current_node.left)
        traverse(current_node.right)

    traverse(root)
    return result


# (Left → Right → Root) --> Down->Top
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def traverse(current_node):
        if not current_node:
            return
        traverse(current_node.left)
        traverse(current_node.right)
        result.append(current_node.val)

    traverse(root)
    return result


from collections import deque


def bfsTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
