# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.


N = int(input("Введите целое число:"))
result = 1

if N < 2 :
    print ("Вы ввели число меньше 2.")
else :
    while N > result:
        result = result*2
        print (f"{result}") 
        if result*2 > N :
            break
