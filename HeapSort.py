from heap import *

def heapSort1(data):
    heap = [0]
    for e in data:
        heappush(heap, e)
        
    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap)
        
def heapify(arr, n, i):
    largest = i
    l =  2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = 1
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapSort(arr):
    n = len(arr)
    print("i = ", 0, arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
        print("i = ", i, arr)
    print()
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("i = ", i, arr)