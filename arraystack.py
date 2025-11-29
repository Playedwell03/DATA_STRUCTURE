class arraystack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity  # 배열 capacity만큼 생성
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity

    def push(self, e):
        if not self.isFull():  # 꽉 차있지 않은 경우에 지정칸 하나 올려 지정칸의 배열을 e로 바꿈.
            self.top += 1
            self.array[self.top] = e
        else:
            pass  # 꽉 차면 패스

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            pass

'''
s = arraystack(10)
for i in range (1,6):
    s.push(i)
print("push 5회 : ", s.array)

s = arraystack(100)

msg = input("문자열 입력 : ")
for c in msg:  # msg 문자열의 각 문자를 스택에 푸시
    s.push(c)
    
print("문자열 출력 : ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()'''