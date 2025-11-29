from LinkedList import *

def hashFn(key):
    return key % M

def insert(key):
    k = hashFn(key)
    n = Node(key)
    n.link = table[k]
    table[k] = n
    
def search(key):
    k = hashFn(key)
    n = table[k]
    while n is not None:
        if n.data == key:
            return n.data
        n = n.link
    return None

def delete(key):
    k = hashFn(key)
    n = table[k]
    before = None
    while n is not None:
        if n.data == key:
            if before == None:
                table[k] = n.link
            else:
                before.link = n.link
            return
        before = n
        n = n.link
    
M = 7
table = [None] * M
insert(251)
insert(300)
insert(20)
insert(50)
print(search(20))
print(search(30))
delete(300)
print(search(300))