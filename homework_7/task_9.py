x = int(input('Введите число x: '))
chis = 1
znam = 1
a = 1
b = 2
res = 1

for i in range(1, 6):
    chis *= (x - a)
    a = 2 * a + 1
chis *= (x - a)

for k in range(1, 7):
    znam *= (x - b)
    b *= 2

if znam != 0:
    print(chis / znam)
else:
    print('На 0 делить нельзя')
