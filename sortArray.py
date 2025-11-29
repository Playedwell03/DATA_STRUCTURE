class sortArray:
    def __init__(self, capacity = 30):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def contains(self, e):
        if e in self.array:
            return True
        else: return False
        
    def append(self, e):
        self.array[self.size] = e
        self.size += 1
        
    def insert(self, e):
        if self.contains(e):
            return 
        
        self.array[self.size] = e
        self.size += 1
        
        for i in range(self.size - 1, 0, -1):
            if self.array[i - 1] <= self.array[i]:
                break
            self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]

    '''def delete(self, e):
        if self.contains(e):
            a = self.array[e]
            for i in range(self.size, , -1)'''

    def __eq__(self, setB):
        if self.size != setB.size:
            return False
        for i in range(0, self.size):
            if not setB.contains(self.array[i]):
                return False
        return True
    
    def union(self, setB):
        setC = sortArray() 
        i = 0
        j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1
        while i < self.size:
            setC.append(self.array[i])
            i += 1
        while j < setB.size:
            setC.append(setB.array[j])
            j += 1
        return setC

a = sortArray()
b = sortArray()

a.insert(3)
a.insert(5)
a.insert(9)
a.insert(2)
b.insert(14)
b.insert(1)
b.insert(4)
b.insert(6)
c = a.union(b)
print(c.array)