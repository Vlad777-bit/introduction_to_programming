import calendar

year = int(input('Введите год, который хотите проверить: '))

if calendar.isleap(year):
    print(f'Результат:\n{year} Високосный год')
else:
    print(f'Результат:\n{year} Обычный год')
