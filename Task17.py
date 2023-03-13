# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Ответ 6
import random

num_of_elem = int(input("Введите количество чисел в списке:"))
list_1 = list()
count = 1

for i in range (num_of_elem):
    list_1.append(random.randint(-10,10)) # Заполняем список случайными значениями
print(list_1)

# Первый способ решения:

# NumOfDifDigit = len(set(list_1))
# print(f"Количество различных чисел {NumOfDifDigit}")



# Второй способ решения:

list_2 = list()

list_2.append(list_1[0])

for i in range (1,len(list_1)):
    flag = True
    for j in range(len(list_2)):
        if list_2 [j] == list_1[i]:
            flag = False
            break
    if flag:
        list_2.append(list_1[i]) 

print(list_2)
print(f"В этом списке {len(list_2)} различных чисел")


