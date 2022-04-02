sign = int(input('Введите кол-во знаков в колонтитуле: '))
exc = int(input('Введите кол-во восклицательных знаков: '))
a = '~' * ((sign - exc)//2)
b = '!' * exc
c = '~' * ((sign - exc)//2)
print(a + b + c)
