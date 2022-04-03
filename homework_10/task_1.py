text = input("Введите текст: ")
letters = 'аоиеёэыуюя'
vowels = [c for c in text if c in letters]
print('Список гласных букв:', vowels)
print('Длина списка:', len(vowels))
