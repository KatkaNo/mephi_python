a = int(input('Введите номер билета: '))
l_sum = 0
r_sum = 0
for i in range(6):
    if i < 3:
        r_sum += a // 10**i % 10
    else:
        l_sum += a // 10**i % 10
if l_sum == r_sum:
    print('Счастливый билет')
else:
    print('Несчастливый билет')
