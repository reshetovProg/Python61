# '''
# 1. При помощи and найти наибольшее из трех
# введенных пользователем чисел
# '''
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)
#
# '''
# 2. Определить является число введенное пользователем четным
# '''
# a = int(input())
# print(a%2==0)
#
#
# '''
# 3. Определить есть ли в двухзначном числе, введенным
# пользователем, цифра 3
# '''
# a = int(input())
# if a//10==3 or a%10==3:
#     print("yes")
# else:
#     print("no")
#
# '''
#
# 4. Определить принадлежит ли число, введенное пользователем,
# диапазону от 10 до 20 включительно
# '''
# a = int(input())
# print(10<=a<=20)
#
# '''
# 5. Пользователь вводит два числа, определить являются ли оба
# числа кратным 3.
# '''
# a = int(input())
# b = int(input())
# print(a%3==0 and b%3==0)

# a=int(input())
# b=int(input())
# if a<b:
#     a,b = b,a
# while a>=b:
#     print(a, end=" ")
#     a=a-1

# a = int(input())
# b = int(input())
# if a>b: a,b=b,a
# if a%2: a+=1
#
# while a<=b:
#     print(a)
#     a+=2
# a = int(input())
# n=0
# if n>a:
#     n,a=a,n
#
# while n<=a:
#     if n % 10 == 3:
#         break
#     n+=1
# while n<=a:
#     if n%10==3:
#         print(n)
#     n+=10

#
# a = int(input())
# n=0
# if n>a:
#     n,a=a,n
#
# flag=True
# while n<=a:
#     if flag:
#         if n % 10 == 3:
#             flag=False
#             continue
#         else:
#             n+=1
#     else:
#         print(n)
#         n+=10

# a=6
# n=0
# while n<=a:
#     if n==3:
#         n+=1
#         break
#     print(n, end=" ")
#     n+=1

n=int(input("сколько чисел: "))
s = 0
while n>0:
    num=int(input("введите число: "))
    s+=num
    n-=1
print(s)