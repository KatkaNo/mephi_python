price = int(input('Введите стоимость квартиры: '))
s = int(input('Введите метраж квартиры: '))
if price <= 10 and s >= 100:
    print('Квартира подходит')
elif price <= 7 and metr >= 80:
    print('Квартира подходит')
else:
    print('Квартира не подходит')