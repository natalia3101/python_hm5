# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
    


if a >= 0 and b >= 0:
    print(sum(a, b))
else:
    print("the numbers cannot be negative")
