a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число с: '))
summ = 0
count = 0
for i in range(a, b +1):
    if i % c == 0:
        count += 1
        summ += i
if count == 0:
    print('Расчет невозможен, так как нет подходящих чисел')
else:
    print(summ / count)
