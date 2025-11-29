def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return -1

def hashFn(key):
    return key % M

def insert(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None:
            break
        i = (i + 1) % M
        count -= 1
    
    if count > 0:
        table[i] = key
        
def search(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None:
            return None
        if table[i] == key:
            return table[i]
        i = (i + 1) % M
        count -= 1
        
    return None

def delete(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == key:
            table[i] = -1
            return
        if table[i] == None:
            return
        i = (i + 1) % M
        count -= 1
    
M = 13
table = [None] * M