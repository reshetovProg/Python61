'''
1. Пользователь вводит два числа, вывести наибольшее из них.
Если числа равны ты написать что
они равны

2. Определить среднюю скорость движения автомобиля.
Пользователь вводит расстояние и время за которое
он его преодолел.

3. Пользователь вводит трехзначное число.
Перевернуть это число и вывести на экран
'''

# num1 = int(input())
# num2 = int(input())
# if num1>num2:
#     print(num1)
# elif num2>num1:
#     print(num2)
# else:
#     print("=")
#
# t = float(input())
# s = float(input())
# print(f"v={s/t}")
#
# n = int(input())
# p1 = n%10
# p2 = n%100//10
# p3 = n//100
# print(p1,p2,p3)

# n1=int(input())
# n2=int(input())
# n3=int(input())
# 5 4 3
# 4 5 3
# 4 3 5
# 3 4 5
# 5 5 4

# if n1>n2:
#     if n1>n3:
#         print(n1)
#     else:
#         print(n3)
# elif n2>n3:
#     print(n2)
# else:
#     print(n3)
#
# if n1>=n2:
#     if n1>=n3:
#         print(n1)
# if n2>=n1:
#     if n2>=n3:
#         print(n2)
# if n3>=n1:
#     if n3>=n2:
#         print(n3)
# n1=2
# n2=3
# n3=4
# if n1>n2>n3:
#     print(n1)
# elif n1>n3>n2:
#     print(n1)
# elif n2>n1>n3:
#     print(n2)
# elif n2>n3>n1:
#     print(n2)
# elif n3>n1>n2:
#     print(n3)
# elif n3>n2>n1:
#     print(n3)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num3:
#     print(num2)
# else:
#     print(num3)

num = int(input())

if 0<=num<=10:
    print("yes")

if num>=0 and num<=10:
    print("yes")

if not(num<0 or num>10):
    print("yes")