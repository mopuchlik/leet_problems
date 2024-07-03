# https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line/


#     1
#     |\
#     2 5
#     /|
#    3 4
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


#     4
#     |\
#     2 5
#     /|
#    1 3
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


#     5
#     |\
#     3 4
#     /|
#    1 2
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
