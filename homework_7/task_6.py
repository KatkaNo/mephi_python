l1 = int(input('Введите размер листа: '))
l2 = l1
convert = 12
i = 0
while convert < l1 or convert < l2:
    if convert < l1:
        i += 1
        l1 = l1 / 2
        if convert < l2:
            i += 1
            l2 = l2 / 2
print('Сложить ', i, 'раз')
