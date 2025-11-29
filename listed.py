class listed:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self):
        return self.size == self.capacity
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size: # <=에서 오류
            for i in range(self.size, pos, -1): #끝에서 pos까지 앞으로오면서
                self.array[i] = self.array[i - 1] #
            self.array[pos] = e
            self.size += 1
        else: 
            print("안됨")
            pass
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            pass
        
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None
        
    def __str__(self):
        return str(self.array[0:self.size])
    
'''
a = listed()

a.insert(0, 10)
a.insert(1, 20)
print(a)
a.delete(0)
a.insert(1, 30)

print(a)
print(str(a.array[::-1]))
'''