import random
# '''
# 1. Посчитать сумму целых чисел от a до b
# '''
# a = int(input())
# b = int(input())
# summa=0
# for i in range (a,b+1):
#     summa+=i
# print(summa)
#
#
# '''
#
# 2. Вывести все целые числа от 0 до n в порядке убывания
# (n может быть как положительным, так и отрицательным)
# '''
# n = int(input())
# if n<0:
#     for i in range(0,n-1,-1):
#         print(i, end=" ")
# else:
#     for i in range(n,-1,-1):
#         print(i, end=" ")
#
# '''
# 3. Посчитать n-факториал
# (произведение чисел от 1 до текущего числа)
# 5! = 1*2*3*4*5=120
# '''
# fact=1
# n = int(input())
# for i in range (2,n+1):
#     fact*=i
# print(fact)
#
#
#
#
# '''
#
# 4. Пользователь вводит 5 чисел. Вывести на экран наибольшее
# '''
#
# max = int(input())
# for i in range(4):
#     a = int(input())
#     if a>max:
#         max=a
# print(max)

# column = int(input())
# row = int(input())
# k=1
# for i in range(row):
#     for j in range (column):
#         print(k, end=" ")
#         k+=1
#     print()

# n = int(input())
# for i in range (n):
#     print("*", end=" ")

# for i in range (3):
#     a = random.randint(0,3)
#     print(a, end=" ")

# n = int(input())
# print("* "*n)
# '''
# for
# '''
# print("* " * n)
# for i in range(n):
#     print("  "*(i)+"* "*(n-i))

n = int(input())
for i in range((n+1)//2):
    print("  "*i+"* "*(n-i*2))