# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

from os import system
system('cls')

number_of_ticket_str = input('Введите номер билета: ')
quantity_of_numbers = len(number_of_ticket_str)
count = 0
sum_first_part = 0
sum_second_part = 0

if quantity_of_numbers % 2 != 0:
    print(f"Билет с номером {number_of_ticket_str} несчастливый, так как его номер нечетный!")
else:
    while count < quantity_of_numbers / 2:
        sum_first_part += int(number_of_ticket_str[count])
        count += 1
    while count < quantity_of_numbers:
        sum_second_part += int(number_of_ticket_str[count])
        count += 1
    if sum_first_part == sum_second_part:
        print(f"Ура!!! Билет с номером {number_of_ticket_str} счастливый!")
    else:
        print(f"Билет с номером {number_of_ticket_str} к сожалению несчастливый!")