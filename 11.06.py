'''
1. Посчитать сумму всех целых чисел от a до b
2. Вывести все целые числа от a до b в порядке убывания
3. Пользователь вводит числа до тех пор, пока не введет 0.
После этого вывести наибольшее из введенных
пользователем чисел
'''
# a = int(input())
# b = int(input())
# if a>b: a,b=b,a
# summa=0
# while a<=b:
#     summa+=a
#     a+=1
# print(summa)
#
# a = int(input())
# b = int(input())
# if a>b: a,b=b,a
# while b>=a:
#     print(b, end=" ")
#     b-=1
# print()

# minimum = 0
# while True:
#     num = int(input())
#     if num==0:
#         break
#     if minimum==0 or minimum>num:
#         minimum=num
# print(minimum)

'''
вводит границы двух диапазонов
вывести все общие числа этих диапазонов
'''
# min1=int(input())
# max1=int(input())
# min2=int(input())
# max2=int(input())
# if min1>max1: min1, max1 = max1, min1
# if min2>max2: min2, max2 = max2, min2
# min = min1>min2 and min1 or min2
# max = max1<max2 and max1 or max2
# # if min1>min2:
# #     min = min1
# # else:
# #     min = min2
# # if max1<max2:
# #     max = max1
# # else:
# #     max = max2
# while min<=max:
#     print(min, end=" ")
#     min+=1
#
#
# a=int(input())
# print(a%2 and "нечетное" or "четное")

# counter=5
# summ=0
# while counter>0:
#     summ+=int(input())
#     counter-=1
# print(summ)

# a=int(input())
# b=int(input())
# if a>b: a,b=b,a
# for i in range (a,b+1,1):
#     print(i,end=" ")

# a=int(input())
# b=int(input())
# mult=1
# for i in range(a,b+1):
#     mult*=i
# print(mult)

# flag = True
# for i in range(5):
#     num = int(input())
#     if flag:
#         maximum = num
#         flag = False
#     else:
#         if maximum<num:
#             maximum = num
# print(maximum)

# num = int(input())
# maximum = num
# for i in range(4):
#     num = int(input())
#     if maximum<num:
#         maximum = num
# print(maximum)

# n = int(input())
# for i in range(n):
#     num = int(input())
#     if num%2==0:

