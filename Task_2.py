# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе? (X+X+2X=Y => 4X=Y => X=Y/4)
from os import system
system('cls')

birds_total = int(input('Сколько всего журавликов сделали дети?: '))
while birds_total % 2 != 0 or birds_total == 2 or int(birds_total / 4) != birds_total / 4:
    print(f'Колличество журавликов должно быть четным и больше двух. Также мальчишки не могут делать одного из журавликов вместе!')
    birds_total = int(input('Так сколько же всего журавликов сделали дети?: '))
print(f'Петя сделал: {birds_total / 4} журавлика(ов).')
print(f'Сережа сделал: {birds_total / 4} журавлика(ов).')
print(f'Катя сделала: {birds_total / 2} журавлика(ов).')