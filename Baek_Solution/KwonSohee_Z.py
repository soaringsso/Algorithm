#백준 1074 Z

def func(x, y, r, c, length):
    result = 0
    if x == r and y == c:
        return result
    if length == 1:
        result += 1
    else:
        result += length * length
        return result


n, r, c = map(int, input().split())
length = pow(2, n)
print(func(0, 0, r, c, length))
