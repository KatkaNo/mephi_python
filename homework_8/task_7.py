string = input('Введите строку: ')
i = 0
lengh = []

for word in string:
    if word != ' ':
        i += 1
        lengh.append(i)
    else:
        i = 0
print ('Самое длинное слово, букв: ',max(lengh))
