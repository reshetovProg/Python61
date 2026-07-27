# # a = int(input())
# #ValueError
# import random
#
# # ls=[2,3]
# # print(ls[2])
# # #IndexError
#
# try:
#     size = int(input())
#     ls=[]
#     for i in range(size):
#         ls.append(random.randint(10,99))
#     index=int(input())
#     print(ls[index])
# except ValueError:
#     print("ошибка типа входных данных")
# except IndexError:
#     print("не существующий индекс")
#
# def summ(*args):
#     summa=0
#     for i in args:
#         summa+=i
#     return summa
#
# def show(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} - {value}")
#
# show(name="Ivan", age=23)

# ls = [2,5,23,5,3,6,8]
# ls2 = [x for x in ls if x%2==0]
ls3 = [int(input()) for i in range(5)]
ls3 = [i for i in ls3 if i<0]
print(ls3)