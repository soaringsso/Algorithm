def merge_two_sorted_lists(A, first, last):
    global Ms, Mc
    m = (first + last) // 2
    i, j = first, m+1
    B = []
    while i <= m and j <= last:
        if A[i] <= A[j]:
            Mc += 1
            B.append(A[i])
            i += 1
        else:
            Mc += 1
            B.append(A[j])
            j += 1
    for k in range(i, m+1): # why?
        B.append(A[k])
        Ms += 1
    for k in range(j, last+1): # why?
        B.append(A[k])
        Ms += 1
    for i in range(first, last+1): # A ← B
        A[i] = B[i - first]
        Ms += 1

def merge_sort(A, first, last):
    if first >= last: 
        return # 정렬 불필요
    m = (first + last) // 2
    merge_sort(A, first, m) # 앞 부분 반 재귀 정렬
    merge_sort(A, m+1, last) # 뒷 부분 반 재귀정렬
    merge_two_sorted_lists(A, first, last)