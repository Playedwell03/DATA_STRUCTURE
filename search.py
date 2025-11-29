def binary_search(A, key, low, high): #배열, 찾을거, 가장 작은 원소, 큰 원소 넣기
    if (low > high): #탐색할 항목 없음
        return -1
    
    middle = (low + high) // 2
    
    if (key == A[middle]): #같으면 반환 후 종료
        return middle
    elif (key < A[middle]):
        return binary_search(A, key, low, middle - 1) #재귀함수, 같지 않으면 key == A[middle - 1]
    else:
        return binary_search(A, key, middle + 1, high) #반대
    
def binary_search_iter(A, key, low, high):
    while(low <= high):
        middle = (low + high) // 2
        
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
            
    return -1