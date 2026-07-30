# import random
#
# # def create_random_set(size):
# #     ls=[]
# #     while size>0:
# #         num=random.randint(1,9)
# #         if num not in ls:
# #             ls.append(num)
# #             size-=1
# #     return ls
# #
# # s1 = set(create_random_set(6))
# # s2 = set(create_random_set(4))
# # print(s1)
# # print(s2)
# # print(len(s1.intersection(s2)))
# # print ((len(s1)+len(s2)-(len(s1.intersection(s2))*2)) > len(s1.intersection(s2))
# #  and "уникальных больше" or "общих больше")
#
# # product = {
# #     "name": "мышка",
# #     "price": 1200.50,
# #     "count": 120,
# #     "colors": ["красный", "синий"]
# # }
# #
# # product["name"]="коврик"
# # product["category"]="аксессуары"
#
# def show_dict(product):
#     for i in product.keys():
#         print(f"{i} - {product[i]}")
#
# disciplines = ["eng","math","rus","lit"]
# def create_student():
#     st={}
#     for i in disciplines:
#         st[i]=[]
#         for j in range(random.randint(3,9)):
#             st[i].append(random.randint(2,5))
#     return st
#
# def avg(list):
#     sum=0
#     for i in list:
#         sum+=i
#     return sum/len(list)
#
# def best_discipline_name(st):
#     max=0
#     disc_name = "unnamed"
#     for i in st.keys():
#         avg_mark=avg(st[i])
#         if max<avg_mark:
#             max=avg_mark
#             disc_name=i
#     return disc_name
#
# def disciplines_with_mark(st):
#     ls = []
#     for i in st.keys():
#         avg_mark=avg(st[i])
#         if 3<=avg_mark:
#             ls.append(i)
#
#     return ls
#
# st1 = create_student()
# show_dict(st1)
# print(f"best disc: {best_discipline_name(st1)}")
# print(f"Оценка больше 3: {disciplines_with_mark(st1)}")
def wor(a):
    lt=a.split(" ")
    result=[]
    for i in lt:
        if lt.count(i)>1:
            if i not in result:
                result.append(i)
    return result
