#백준 1181 권소희

n = int(input())
word = []
for i in range(n):
    w = input()
    word.append(w)


word.sort(key=lambda x : len(x)) 
new_word = set(word)

print(new_word)
