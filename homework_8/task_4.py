row = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений в ряду: '))
whitespace = int(input('Введите кол-во метров между рядами: '))
print()
print('Сцена')
print()
for i in range(row):
    print('=' * seat, '*' * whitespace, '=' * seat)
