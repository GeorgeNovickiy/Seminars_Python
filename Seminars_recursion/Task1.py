# 1. Дано натуральное число *N* и последовательность из *N* элементов. 
# Требуется вывести эту последовательность в обратном порядке.

# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

n = int(input("Введите количество элементов последовательности:"))

def printR(m):
    x = int(input("Введите элемент последовательности:"))
    if m!= 0:
        printR(m-1)
    print(x)

printR(n)