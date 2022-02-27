exp = int(input('Введите количество опыта: '))
if exp < 1000:
    print('Уровень героя: ', 1)
elif exp >= 1000 and exp < 2500:
    print('Уровень героя: ', 2)
elif exp >= 2500 and exp < 5000:
    print('Уровень героя: ', 3)
else:
    exp >= 5000
    print('Уровень героя: ', 4)