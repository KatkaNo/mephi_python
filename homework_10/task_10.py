txt = input('Введите сообщение: ')
key = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
new_txt = []
for symbol in txt:
    if symbol in alphabet:
        new_txt.append(alphabet[(alphabet.find(symbol) + key) % len(alphabet)])
    else:
        new_txt.append(symbol)
print('Зашифрованное сообщение:', ''.join(new_txt))