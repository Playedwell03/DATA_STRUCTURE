class CircularQueue:
    def __init__(self, capacity = 8): #큐를 생성
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0 #front -> 삭제되는곳
        self.rear = 0 #rear -> 추가되는곳
        
    def isEmpty(self):
        return self.front == self.rear #front와 rear가 같으면 공백이다.
    
    def isFull(self): 
        return self.front == (self.rear + 1) % self.capacity #front가 rear의 다음칸인지
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass
        
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] + \
                self.array[0:self.rear + 1])
#(self.rear + 1) % self.capacity -> +1로 하면 7번째 배열에서 0번째 배열로 못간다.
'''
q = CircularQueue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')
q.enqueue('E')
q.enqueue('F')

print('A B C D E F 삽입 : ', q)
print('삭제 -->', q.dequeue())
print('삭제 -->', q.dequeue())
print('삭제 -->', q.dequeue())
print('     3번의 삭제 : ', q)
q.enqueue('G')
q.enqueue('H')
q.enqueue('I')

print('     G H I 삽입 : ', q)'''