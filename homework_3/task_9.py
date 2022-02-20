exp = int(input('Пробег:'))
day = int(input('День:'))
sum = exp // 100 + exp % 100 // 10 + exp % 10
if sum>day:
    print('Сброс')
else:
    print('Сегодня не сломался')
