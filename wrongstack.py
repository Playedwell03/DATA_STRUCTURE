class arraystack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity #배열 capacity만큼 생성
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top == self.capacity 

    def push(self, e):
        if not self.isFull():
            self.array[self.top] = e
            self.top += 1
        else: pass
    
    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top - 1]
            self.top -= 1
            return e
        else: pass
    
s = arraystack(100)

msg = input("문자열 입력 : ")
for c in msg:
    s.push(c)
    
print('현재 스택의 개수는 : ', s.top)
    
print("문자열 출력 : ", end = '')
while not s.isEmpty():
    print(s.pop(), end = '')
print()

print('현재 스택의 개수는 : ', s.top)