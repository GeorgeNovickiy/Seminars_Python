# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

n = int(input("Введите целое неотрицательное число:"))
count = 1
result = 1

if n == 0:
    print(f"{n}! = 1")
else :
    while count < n:
        result = result * (count +1)
        count+=1
    print (f"{n}! = {result}")
