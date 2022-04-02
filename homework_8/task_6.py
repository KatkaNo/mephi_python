string = input() + 'oops'
a = []
k = 0
for i in string:
    if i == 's':
        k += 1
    else:
        a.append(k)
        k = 0
print('Самая длинная последовательность: ', max(a))
