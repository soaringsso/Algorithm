def find_median_five(L):
    for i in range(4):
        for j in range(i+1, 5):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L[2]
    

def MoM(L, k):  #L의 값 중에서 k번째로 작은 수 리턴
    if len(L) == 1:
        return L[0]
    i = 0
    A, B, M, medians = [], [], [], []
    while i+4 < len(L):
        medians.append(find_median_five(L[i:i+5]))
        i+=5
    if i < len(L) and i+4 >= len(L):
        for j in range(len(L)-i-1):
            for l in range(j+1, len(L)-i):
                if L[i+j] > L[i+l]:
                    L[i+j], L[i+l] = L[i+l], L[i+j]
        if (len(L)-i) % 2 == 0:
            medians.append((L[(len(L)+i)//2] + L[(len(L)+i)//2 - 1]) // 2)
        else:
            medians.append(L[(len(L)+i)//2])

    mom = MoM(medians, len(medians)//2)
    for v in L:
        if v < mom :    A.append(v)
        elif v > mom:   B.append(v)
        else:   M.append(v)

    if len(A) >= k :    return MoM(A, k)
    elif len(A) + len(M) < k :  return MoM(B, k- len(A)-len(M))
    else:   return mom


n, k = map(int, input().split())    #n과 k를 입력의 첫 줄에서 읽어들인다
L = [int(x) for x in input().split()] #n개의 정수를 읽어들인다(split 이용 + int로 변환)
print(MoM(L, k))