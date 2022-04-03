from random import uniform

first = list(round(uniform(5, 10), 2) for i in range(20))
second = list(round(uniform(5, 10), 2) for k in range(20))
winners = list()
for j in range(len(first)):
    if first[j] > second[j]:
        winners.append(first[j])
    else:
        winners.append(second[j])
print("Первая команда: ", first)
print("Вторая команда: ", second)
print("Победители: ", winners)
