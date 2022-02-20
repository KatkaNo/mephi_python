hours = int(input('Кол-во часов:'))
credit = int(input('Остаток по кредиту:'))
food = int(input('Денег на еду:'))
salary = (200 * hours) / (2**3) + hours
if salary >= credit + food:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')
