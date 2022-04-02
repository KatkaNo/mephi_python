n = int(input('Введите количество должников: '))
summary = 0
for i in range (0, n + 1, 5):
    print('Должник с номером ', i)
    rest = int(input('Сколько должны? '))
    summary += rest
print('Общая сумма долга: ',summary)
