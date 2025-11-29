from nodetree import *

def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def insert_avl(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)
        
    bf = calc_height_diff(root)
    
    if bf > 1:
        if node.key < root.left.key:
            return rotateLL(root)
        else:
            return rotateLR(root)
        
    elif bf < -1:
        if node.key < root.right.key:
            return rotateRL(root)
        else:
            return rotateRR(root)
        