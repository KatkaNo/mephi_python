summ = 0
for i in range(1, 13):
   av = float(input(f"Зарплата за месяц №{i}: "))
   summ += av
print("Средняя зарплата за год:", summ / 12)