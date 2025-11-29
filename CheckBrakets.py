from arraystack import arraystack

def checkBrackets(statement):
    stack = arraystack(100)
    
    for ch in statement:
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch) #ch번째 배열에 스택추가
            
        elif ch == '}' or ch == ']' or ch == ')':
            if stack.isEmpty():
                return False 
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "("):
                    return False
    return stack.isEmpty()

s1 = "{a + b) = c}"
s2 = "[(i am a big boy) haha{ baby}"
s3 = "(123)"


print(s1, "--->", checkBrackets(s1))
print(s2, "--->", checkBrackets(s2))
print(s3, "--->", checkBrackets(s3))
#6.29368