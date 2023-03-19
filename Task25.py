# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался.
#  Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_



inStr = "a a a b c a a d c d d"
count = {}

for ch in inStr.split():
    if ch in count:
        count[ch] +=1
    else:
        count[ch] = 1



outString = ""

for key in count:
    for i in range(count[key]):
        if i == 0:
            outString += key + " "
        else: 
            outString += key + "_" + str(i) + "_"

print(outString)
