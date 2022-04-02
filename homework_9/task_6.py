N = int(input('Кол-во чисел: '))
lst = list()
for i in range(int(N)):
    a = int(input('Число: '))
    lst.append(a)
print ('Последовательность: ',lst)
for i in range(len(lst)):
    if lst[i:] == lst[i:][::-1]:
        print('Нужно приписать чисел: ',i)
        print('Сами числа: ',lst[:i][::-1])
        break
