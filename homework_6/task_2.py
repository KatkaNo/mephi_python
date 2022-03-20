a = 0
for n in range(10):
    n = int(input('Введите число: '))
    if n % 2 == 0 and n > 0:
        a += 1
print('Число четных и положительны номеров = ', a)
