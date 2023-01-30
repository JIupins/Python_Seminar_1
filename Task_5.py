# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. Через строку решать нельзя

from os import system
system('cls')

num_str = input('Веедите число: ')
num = float(num_str)
lenght_number = len(num_str)
lenght_whole_part = len(str(int(num)))
sum = 0

if lenght_number > lenght_whole_part:
    num = num * 10 ** (lenght_number - lenght_whole_part + 1)

while num > 0:
    sum += (num % 10)
    num //= 10

print(f'Сумма цифр в числе {num_str} равна: {int(sum)}')