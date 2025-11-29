from nodetree import *

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    result = search_value_bst(n.left, value)
    if result is not None:
        return result
    else:
        return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
        
    else:
        root.right = insert_bst(root.right, node)
        
    return root

def delte_bst(root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delte_bst(root.left, key)
    elif key > root.key:
        root.right = delte_bst(root.right, key)
        
    else: 
        if root.left == None: #case 1
            return root.right
        
        if root.right == None: #case 2
            return root.left
        
        #case3
        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delte_bst(root.right, succ.key)
        
    return root

class BSTMap():
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root == None
    
    def findMax(self):
        return search_max_bst(self.root)
    
    def findMin(self):
        return search_min_bst(self.root)
    
    def search(self, key):
        return search_bst(self.root, key)
    
    def searchValue(self, value):
        return search_value_bst(self.root, value)
    
    def insert(self, key, value = None):
        n = BSTNode(key, value)
        self.root = insert_bst(self.root, n)
        
    def delete(self, key):
        self.root = delte_bst(self.root, key)
        
    def display(self, msg = 'BSTMap : '):
        print(msg, end = '')
        inorder(self.root)
        print()