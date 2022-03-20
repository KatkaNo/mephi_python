sum = 0
shop = 0
for i in range(8):
    task = int(input('Сколько задач решит Максим? '))
    shop = int(input('Звонит жена. Взять трубку? '))
    sum += task
    shop += shop
print('Рабочий день закончился. Всего выполнено задач: ',sum)
if shop >= 1:
    print('Нужно зайти в магазин.')
else:
    print('В магазин заходить не нужно.')
