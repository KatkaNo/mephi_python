from random import randint

n = int(input('Кол-во элементов: '))
s = [randint(-1, 1) for i in range(n)]
print(s)
j = len(s) - 1
for i in range(len(s)):
    if s[i] == 0:
        while j > i:
            if s[j] == 0:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                j -= 1
                break
        else:
            break
print(s)
