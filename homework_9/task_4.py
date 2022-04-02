n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', k, 'человек.')
people = list(range(1, n + 1))
looser = 0
for _ in range(n - 1):
    print('Текущий круг людей', people)
    first = looser % len(people)
    looser = (first + k - 1) % len(people)
    print('Начало счёта с номера', people[first])
    print('Выбывает человек под номером', people[looser])
    people.remove(people[looser])
    print()
print('Остался человек под номером', people)
