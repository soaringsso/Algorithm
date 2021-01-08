def min_max_slicing(A):
    n = len(A)
    if n <= 2:
        if A[0] < A[-1]:
            return A[0], A[-1]
        return A[-1], A[0]
    left_min, left_max = min_max_slicing(A[:n//2]) #왼쪽 반의 최소, 최대
    right_min, right_max = min_max_slicing(A[n//2:]) #오른쪽 반의 최소, 최대
    mini = left_min
    maxi = left_max
    if right_min < mini:
        mini = right_min
    if  maxi < right_max:
        maxi = right_max
    return mini, maxi

A = [int(x) for x in input().split()] #n개의 정수를 읽어 A에 저장
m, M = min_max_slicing(A)
print(m, M) 


def min_max_indexing(A, left, right):
    if right <= (left + 1):
        if A[left] < A[right]:
            return A[left], A[right]
        return A[left], A[right]
    mid = (left + right) / 2
    left_min, left_max = min_max_indexing(A, left, mid) #왼쪽 반의 최소, 최대
    right_min, right_max = min_max_indexing(A, mid+1, right) #오른쪽 반의 최소, 최대
    mini = left_min
    maxi = left_max
    if right_min < mini:
        mini = right_min
    if  maxi < right_max:
        maxi = right_max
    return mini, maxi

A = [int(x) for x in input().split()] #n개의 정수를 읽어 A에 저장
m, M = min_max_indexing(A, 0, len(A)-1)
print(m, M) 
