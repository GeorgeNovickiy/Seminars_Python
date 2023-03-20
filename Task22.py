# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов множества n:"))
m = int(input("Введите количество элементов множества m:"))

list_1 = []
list_2 = []

for i in range (n):
    list_1.append(int(input(f"Введите {i} Элемент множества list_1:")))

for j in range (m):
    list_2.append(int(input(f"Введите {j} Элемент множества list_2:")))

print (f"1 множество чисел : {list_1}")
print (f"2 множество чисел : {list_2}")

uniq1 = set(list_1)
uniq2 = set(list_2)

union = uniq1.union(uniq2)

print (f"Результат : {union}")

