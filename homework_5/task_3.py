a = int(input())
n = 1
while a // 10 >= 1:
    n += 1
    a //= 10
print(n)