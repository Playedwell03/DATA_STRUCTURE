class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link #node.link = (node.link).link
            pos -= 1
        return node
    
    def getEntry(self, pos): #위치의 노드 반환
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def insert(self, pos, elem): 
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head) #가장 처음 만드는 노드. head설정
        else:
            node = Node(elem, before.link) #node라는 노드생성. 전의 링크와 이어준다
            before.link = node
            
    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None: 
            if self.head is not None:
                self.head = self.head.link 
            
        elif before.link != None: #지정한곳에 요소가 있으면 그 전 요소의 링크를 그 다음걸로 이음
            before.link = before.link.link
            
'''            
a = LinkedList()
a.insert(0, 15)
print(a.head.data)
a.insert(1, 13)
print(a.head.data)
a.insert(2, 28)
print(a.getEntry(2))
print(a.head.data)
a.delete(1)
print(a.getEntry(1))
'''