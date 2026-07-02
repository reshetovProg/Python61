import random
# '''
# создать список из десяти нулей
# 1. заменить все числа рандомными значениями в диапазоне
# от a до b
# 2. найти среди этих значений наибольшее и вывести его индекс
# 3. создать второй список такого же размера как первый и
# переписать в него все четные значения из первого.
# ВНИМАНИЕ
# list1 = [2,5,4,6,5,6,5,5,7,7,7,8]
# list2 = [0,0,0,0,0,0,0,0,0,0,0,0]
# после выполнения кода, список должен стать таким:
# list2 = [2,4,6,6,8,5,5,5,5,7,7,7]
# import random
# random.randint(a,b)
#
# '''
#
# a = int(input('начальная граница диапазона: '))
# b = int(input('верхняя граница диапазона: '))
# list1 = [0,0,0,0,0,0,0,0,0,0]
# for i in range (len(list1)):
#     list1[i]=random.randint(a,b)
# print(list1)
#
# max=list1[0]
# max_index=0
# for i in range (len(list1)):
#     if list1[i] > max:
#         max = list1[i]
#         max_index = i
#
# print(f"значение: {max} индекс: {max_index}")
#
# list2 = [0,0,0,0,0,0,0,0,0,0]
# n=0
# for i in range(len(list1)):
#     if list1[i]%2==0:
#         list2[n]=list1[i]
#         n+=1
#
# for i in range(len(list1)):
#     if list1[i]%2!=0:
#         list2[n]=list1[i]
#         n+=1
#
# print(list1)
# print(list2)

# def show_list():
#     print()
#     for i in list1:
#         for j in i:
#             print(j, end="\t")
#         print()
#
# list1 = [[23,5,3,5,2,5,3,6],
#         [23,5,39,5,2,58,3,6],
#         [23,5,34,5,2,54,3,6]]
#
# show_list()
# list1[2][3]=999
# show_list()

def maximum(list1):
    max=list1[0]
    for i in range (len(list1)):
        if list1[i] > max:
            max = list1[i]

    return max
#
# def generate_random_list(list1):
#     for i in range(len(list1)):
#         list1[i]=random.randint(1,99)
#
# def change_a(a):
#     a+=1
# students = [2,4,3,5,3,5,2]
# generate_random_list(students)
# print(students)
# print(maximum(students))
# a=6
# change_a(a)
# print(a)
#
# def change_list(a):
#     a[0]=2
#
# list1 = [5,5,3]
# change_list(list1)
# print(list1)

def aver(list1):
    summ=0
    for i in list1:
        summ+=i
    return summ/len(list1)

school = [[2,3,5,2,5,4,6,3],
          [2,4,5,3],
          [2,5,4,4,48,4,4],
          [2,4,5,3]]

# summa=0
# for i in school:
#     summa+=aver(i)
# print(summa/len(school))

max = 0
index_max=0
for i in range (len(school)):
    if max<maximum(school[i]):
        max = maximum(school[i])
        index_max = i
print(index_max)
