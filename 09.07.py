# def str_cut(st):
#     if st.find("begin")==-1 or st.find("end")==-1:
#         return ""
#     return st[st.find("begin")+5: st.find("end")]

# st = "апельсин мандарин апельсин тоже фрукт что и мандарин"
# list = st.split(" ")
# st2=""
# print(list)
# for i in list:
#     if i!="" and i[-1]=="л":
#         i+="а"
#     st2+=i+" "
# st2 = st2.strip()
# print(st2)

# ls ="hdfsaj jh jasdfjh    asdjfhjhasf    "
# str=""
# s = set(ls.split(" "))
# for i in s:
#     if i !="":
#         str+=i+" "
# print(str.strip().split(" "))

st = "weiudgwi134iuh1i234ii12h4h 14 i 214i i1 4ii1"
counter=0
for i in st:
    if i.isdigit():
        counter+=1
print(counter)




# for i in st:
#     if i[-3:]=="вна":
#         print(i)