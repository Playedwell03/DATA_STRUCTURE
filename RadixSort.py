from queue import Queue

def radix_sort(A):
    queues = []
    for i in range(BUCKETS): #BUCKETS개의 큐 사용
        queues.append(Queue())
        
    n = len(A)
    factor = 1 #1의 자리부터 시작
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].put(A[i])
        i = 0
        
    for b in range(BUCKETS):
        while not queues[b].empty():
            A[i] = queues[b].get()
            i += 1
    factor *= BUCKETS #다음 자릿수로 이동
    print("step", d + 1, A)
    
    BUCKETS = 1
    DIGITS = 1