#백준 1931 회의실배정 
def func(list):   #빨리 끝나는 것 중 빨리 시작 
    result = 1  #몇 개의 회의를 하게 될 것인지를 저장
    result_list = []    #회의를 갖게될 리스트를 추가함
    n = len(list)
    result_list.append(list[0]) #0번째 리스트를 추가
    j, i = 0, 0
    while(1):
        i += 1
        if i == n:
            break
        if list[j][1] <= list[i][0]:
            result_list.append(list[i])
            result += 1
            j = i
    return result
    

n = int(input())
x = [[0 for _ in range(2)] for _ in range(n)] #이중리스트 선언 
for i in range(n):
    a, b = map(int, input().split())
    x[i][0] = a
    x[i][1] = b
list = sorted(x, key = lambda x : (x[1], x[0])) 
#이중리스트에서 2번째 인자를 기준으로 오름차순한 후, 1번째 인자를 기준으로 오름차순

print(func(list))