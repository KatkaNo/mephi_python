a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
print(c)