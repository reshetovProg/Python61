import random
#
# ls = []
# n = int(input())
# for i in range(n):
#     ls.append(random.randint(1,9))
# print(ls)

def remove_all(ls, a):
    i=0
    size = len(ls)
    while i<size:
        if ls[i]==a:
            ls.remove(a)
            size-=1
            i-=1
        i+=1

# def remove_all_pop(ls, a):
#     i=0
#     size = len(ls)
#     while i < size:
#         if ls[i]==a:
#             ls.pop(i)
#             size -= 1
#             i -= 1
#         i+=1
#
# ls = [2,4,2,4,2,2,2,4,5,2,2]
#
# ls.sort()
# remove_all_pop(ls, 2)
# print(ls)
#
# ls1=[2,3,4,5]
# ls2=[]
# ls2.extend(ls1)
# # ls2 = ls1.copy()
# ls2[2]=5
# print(ls1)
# print(ls2)

students = []
students_marks=[]

while True:
    var = int(input('''1 - добавить ст, 
    2 - удалить ст, 
    3 - вывести инфу,
    4 - добавить оценку,
    5 - изменить оценку\n'''))
    if var==1:
        name = input("введите имя студента: ")
        students.append(name)
        students_marks.append([])
    elif var==2:
        index = int(input("введите номер студента для удаления: "))
        if 1<=index<=len(students):
            students.pop(index-1)
            students_marks.pop(index-1)
        else:
            print("такого студента нет")
    elif var==3:
        for i in range (len(students)):
            print(f"{i+1}. {students[i]}: {students_marks[i]}")
    elif var==4:
        index = int(input("введите номер студента: "))
        if index<1 or index>len(students):
            print("не корректный номер студента")
        else:
            mark = int(input("введите оценку: "))
            students_marks[index-1].append(mark)
    elif var == 5:
        index = int(input("введите номер студента: "))
        if index < 1 or index > len(students):
            print("не корректный номер студента")
        else:
            index_mark = int(input("какую оценку поменять "))
            if len(students_marks[index-1])< index_mark:
                print(" такой оценки нет ")
            else:
                mark = int(input("введите оценку: "))
                students_marks[index-1][index_mark]=mark
    else:
        break

