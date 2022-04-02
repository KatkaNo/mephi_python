string = input('Введите строку из букв a и b, лат. буквами: ')
milk = 0
for i in range(10):
    if string[i] == 'b':
        milk += 2 * (i + 1)
print('Молока всего: ', milk)
