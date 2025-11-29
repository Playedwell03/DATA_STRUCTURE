class Set:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def contains(self, e):
        if e in self.array:
            return True
        else: return False
    
    def insert(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else: pass
        
    def delete(self, e):
        if not self.isEmpty():
            for i in range(0, self.size):
                if self.array[i] == e:
                    a = self.array[i]
                    for i in range(i, self.size):
                        self.array[i] = self.array[i + 1]
            self.size -= 1
            return a 
        
    def shortdelete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return
        
    def __str__(self):
        return str(self.array[:self.size])
    
    def union(self, setB):
        setC = Set()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB):
                setC.insert(setB.array[i])
        return setC
    
    def intersect(self, setB):
        setC = Set()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self, setB):
        setC = Set()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
s = Set()

s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
print(s.contains(60))
s.delete(40)
print(s)

g = Set()

g.insert(50)
g.insert(30)
g.insert(100)

print(s.union(g))
print(s.intersect(g))
print(s.difference(g))