def dp_quick_sort(A, low, high):
    if low < high:
        lp, rp = partitionDP(A, low, high)
        dp_quick_sort(A, low, lp - 1)
        dp_quick_sort(A, lp + 1, rp - 1)
        dp_quick_sort(A, rp + 1, high)
        
def partitionDP(A, low, high):
    if A[low] > A[high]:
        A[low], A[high] = A[high], A[low]
        
    j = low + 1
    g = high - 1
    k = low + 1
    lpVal = A[low]
    rpVal = A[high]
    
    while (k <= g):
        if (A[k] < lpVal):
            A[k], A[j] = A[j], A[k]
            j += 1
            
        elif (A[k] >= rpVal and k < g):
            while (A[g] > rpVal and k < g):
                g -= 1
            A[k], A[g] = A[g], A[k]
            g -= 1
            
            if (A[k] < lpVal):
                A[k], A[j] = A[j], A[k]
            k += 1
            
    j -= 1
    g += 1
    A[low], A[j] = A[j], A[low]
    A[high], A[g] = A[g], A[high]
    
    return j, g