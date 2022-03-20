allert = 0
for i in [30,31,32,33,34,35]:
    a=int(input())
    print ('Людей в',i,'секторе: ',a)
    if a>9:
        print('Нарушение! Слишком много людей в секторе!')
        allert += 1
    else:
        print('Всё спокойно.')
print('Количество нарушений:',allert)
