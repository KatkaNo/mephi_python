text = input('Введите строку: ')
reversed_fragment = text[text.find('h') + 1:text.rfind('h')]
text = reversed_fragment[::-1]
#признаюсь, методы find и rfind подсмотрела в инете. Сама пыталась решить через циклы.
