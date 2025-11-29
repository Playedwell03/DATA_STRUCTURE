from LinkedStack import Node

class LinkedQueue:
    def __init__(self):
        self.tail = None #tail = 삽입하는곳
        
    def isEmpty(self):
        return self.tail == None
    
    def isFull(self):
        return False
    
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.tail = node #만든 노드를 꼬리로
            node.link = node #node.link가 만든 노드를 가리키게
        else:
            node.link = self.tail.link 
            self.tail.link = node
            self.tail = node
            
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail: #노드가 하나일경우 전부 삭제되었으니 None.
                self.tail = None
            else:
                self.tail.link = self.tail.link.link #하나가 아니면 tail의 link를 프론트 다음의 노드로 이어줌. 
            return data
        
a = LinkedQueue()

a.enqueue(13)
print(a.tail.link.data)
a.enqueue(15)
print(a.tail.link.data)
a.enqueue(17)
print(a.tail.link.data)

#a.tail.link.data 결과는 전부 다 가장 처음 생성한 데이터를 가리키고 있는것 확인.
