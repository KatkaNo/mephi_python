n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
bahn = ['|'] * n
for i in range(k):
    print('Бросок', i+1)
    left = int(input('Сбиты палки с номера '))
    right = int(input('по номер '))
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))
