number = int(input())
if number % 2 == 0 and number % 3 != 0:
    print(number, 'Число подходит')
else:
    print('Число не подходит')