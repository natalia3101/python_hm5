# Задача 26:  Напишите программу, которая на 
# вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A = int(input("Enter a number: "))
B = int(input("Enter the exponentiation: "))


def to_power(A, B):
    if B == 1:
        return A
    elif B == 0:
        return 1
    return A * to_power(A, B - 1)

if B < 0:
    print("Enter a positive number")
else:
    print(to_power(A, B))