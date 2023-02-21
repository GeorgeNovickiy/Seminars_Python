# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

x = int(input("Введите трехзначное число:"))

firstDigit = int(x%10)
secondDigit = int((x%100)//10)
thirdDigit = int(x//100)

result = firstDigit+secondDigit+thirdDigit
print (f"Сумма цифр числа {x} равна {result}")