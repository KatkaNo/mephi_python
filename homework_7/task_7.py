educational_grant = int(input('Введите размер степендии: '))
expenses = int(input('Введите расходы на проживание: '))
mounth = 10
summ = expenses
for i in range(2, mounth + 1):
    expenses = expenses * 1.03
    summ = summ + expenses
print('У родителей необходимо попросить: ', (summ - educational_grant * mounth) // 1 + 1, 'рублей')
