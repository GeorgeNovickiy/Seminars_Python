# Написать функцию вычисления факториала числа n:

n = int(input("Введите число:"))

def fact(m):
    if m == 1:
        return 1
    return m * fact(m-1)

print(f"Факториал числа {n} = {fact(n)}") 