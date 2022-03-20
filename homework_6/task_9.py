prev = 0
for month in range(10):
  next = int(input())
  if next < prev:
    print('Не упорядчоенно')
    break
  prev = next
else:
  print('Упорядчоенно')