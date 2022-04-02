x = 8
y = 10
where = input('Марсоход находится на позиции 8, 10 введите команду: ')

while x != -1 and y != -1:
    if x < 15 and y <20:
        if where == 'w':
            y += 1
            print('Марсоход находится на позиции', x, y,'введите команду: ', end='')
            where = input()
        elif where == 's':
            y -= 1
            print('Марсоход находится на позиции', x, y,'введите команду: ', end='')
            where = input()
        elif where == 'a':
            x -= 1
            print('Марсоход находится на позиции', x, y,'введите команду: ', end='')
            where = input()
        elif where == 'd':
            x += 1
            print('Марсоход находится на позиции', x, y,'введите команду: ', end='')
            where = input()
    else:
        if where == 'w':
            y += 1
            print('Марсоход находится на границе', x, y,'введите команду: ', end='')
            where = input()
        elif where == 's':
            y -= 1
            print('Марсоход находится на границе', x, y,'введите команду: ', end='')
            where = input()
        elif where == 'a':
            x -= 1
            print('Марсоход находится на границе', x, y,'введите команду: ', end='')
            where = input()
        elif where == 'd':
            x += 1
            print('Марсоход находится на границе', x, y,'введите команду: ', end='')
            where = input()
