#백준 18238 권소희

L = input()
start = 'A'
result = 0

for i in range(len(L)): #0-25 
    m = min(abs(ord(start) - ord(L[i])), 26 - abs(ord(start) - ord(L[i])))
    result += m
    start = L[i]

print(result)