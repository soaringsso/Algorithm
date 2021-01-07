def Min(arr):
    S = 0
    result = []
    arr.sort()
    for i in range(len(arr)):
        S += int(arr[i])
        result.append(S)
    return sum(result)


n = int(input())
arr = [int(x) for x in input().split()]
print(Min(arr))