def quick_select(L, k): #L에 있는 수 중에서 k번째로 작은 수 리턴
    p = L[0]    #pivot
    A, B, M = [], [], []
    for x in L:
        if x < p:
             A.append(x)
        elif x > p:
             B.append(x)
        else:
             M.append(x)
    if len(A) >= k:
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k-len(A)-len(M))
    else:
        return p


n, k = map(int, input().split())    #n:입력할 정수의 개수  #k:몇번째 정수인지
L = list(map(int, input().split()))

print(quick_select(L, k))