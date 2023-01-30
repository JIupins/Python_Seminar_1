# Найдите сумму цифр трехзначного числа.

from os import system
system('cls')

num_ini = int(input('Веедите целое число: '))
num = num_ini
sum = 0

while num > 0:
    sum += (num % 10)
    num //= 10

print(f'Сумма цифр в числе {num_ini} равна: {sum}')
