class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def insert(self, pos, item):
        return Node