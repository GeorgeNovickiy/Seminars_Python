# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, 
#  чтобы все монетки были повернуты вверх одной и той же стороной. 
#  Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монеток:"))
count0 = 0
count1 = 0

for i in range(n):
    money = random.randint(0, 1)
    print(money)
    if money > 0 :
        count1 +=1
    else :
        count0 +=1
if count1 >= count0:
    print (f"Минимальное количество монет, которое нужно перевернуть {count0}")
else :
    print (f"Минимальное количество монет, которое нужно перевернуть {count1}")

