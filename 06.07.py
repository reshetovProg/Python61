# a = int(input())
# b = int(input())
# if a>b: a,b=b,a

# list = [4,2]
# if list[0]>list[1]:
#     list[0],list[1]=list[1],list[0]
# print(list)
#
# def swap(list, index1, index2):
#     list[index1],list[index2]=list[index2],list[index1]
#
#
# counter=0
# list = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
# for j in range(len(list)-1):
#     for i in range(len(list)-1):
#         counter+=1
#         if list[i]>list[i+1]:
#             swap(list,i,i+1)
# print(list)
# print(f"итераций:{counter}")
#
# counter=0
# list = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
# for j in range(len(list)-1):
#     for i in range(len(list)-1-j):
#         counter += 1
#         if list[i]>list[i+1]:
#             swap(list,i,i+1)
# print(list)
# print(f"итераций:{counter}")
#
# counter=0
# list = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
# for j in range(len(list)-1):
#     flag=False
#     for i in range(len(list)-1-j):
#         counter += 1
#         if list[i]>list[i+1]:
#             flag=True
#             swap(list,i,i+1)
#     if not flag:
#         break
# print(list)
# print(f"итераций:{counter}")
#
#
# counter=0
# list = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
#
# for i in range (1,len(list)):
#     for j in range (i, 0, -1):
#         counter += 1
#         if list[j]<list[j-1]:
#             swap(list, j, j-1)
#         else:
#             break
#
# print(list)
# print(f"итераций:{counter}")
#
# list = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
#
# list.sort()
# print(list)

# a = 5
# def name_function(a):
#
#     print(a,end=" ")
#     a-=1
#     if a>0:
#         name_function(a)
#     print(a, end=" ")
#
# name_function(a)

# def summa(s=0):
#     num = int(input())
#     s+=num
#     if num==0:
#         return s
#     else:
#         return summa(s)
# print(summa())

#
#
#
#
# def d(name, game="dota"):
#     print(f"игрок: {name} игра: {game}")
#
# d("CS")
# d()



def show(list, index=0):
    print(list[index],end=" ")
    if index<len(list)-1:
        show(list, index+1)

list = [2,3,2,5,6]
show(list)
