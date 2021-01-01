def make_heap(A):
    n = len(A)
    for k in range(n//2-1, -1, -1):
        heapify_down(A, k, n)

def heapify_down(A, k, n):
    global Hs, Hc
    while 2*k+1 < n:
        L, R = 2*k + 1, 2*k + 2
        if L < n and A[L] > A[k]:
            Hc += 1
            m = L
        else :
            Hc += 1
            m = k
        if R < n and A[R] > A[m]:
            Hc += 1
            m = R
        if m != k: 
            A[k], A[m] = A[m], A[k]
            Hs += 1
            k = m
        else : 
            break 

def heap_sort(A):
    global Hs, Hc
    n = len(A)
    make_heap(A)
    for k in range(n-1, -1, -1):
        A[0], A[k] = A[k], A[0]
        Hs += 1
        n -= 1
        heapify_down(A, 0, n)
        
