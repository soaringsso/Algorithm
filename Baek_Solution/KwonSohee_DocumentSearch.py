#백준 1543 권소희

def func(doc, sch):
    a = doc.replace(sch, "1")   #doc에서 sch를 찾고 1로 바꿔줌
    result = a.count('1')   #바뀐 1의 개수를 찾아줌
    return result

doc = str(input())  #문서 입력
sch = str(input())  #검색하고 싶은 단어 입력

print(func(doc, sch))