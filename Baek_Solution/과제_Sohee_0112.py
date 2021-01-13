#과제2 가장 큰 수 찾기 권소희 

def solution(numbers):
    answer = ''
    f_answer = ''
    numbers = list(map(str, numbers))

    for i in numbers:
        if len(i) == 4:
            answer.append([i,i*3])
        if len(i) == 3:
            answer.append([i,i*4])
        if len(i) == 2:
            answer.append([i,i*6])
        if len(i) == 1:
            answer.append([i,i*12])

    #numbers.sort(key = lambda x : x*3, reverse=True)
    #이런 간단한...식이..있었군..
    for i in numbers:
        f_answer.append(i[0])

    if len(numbers) == numbers.count('0'):
        return '0'
    else:
        answer = "".join(f_answer)
        return f_answer

numbers = [int(x) for x in input().split()]
print(solution(numbers))
