import random
#1

a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
max = a1
if max<a2: max=a2
if max<a3: max=a3
if max<a4: max=a4
print(max)

#2
a=int(input())
b=int(input())
if a>b: a,b=b,a
for i in range(b, a-1, -1):
    print(i,end=" ")

#3
size = int(input())
count=5
for i in range(size):
    for j in range(size):
        print(count, end=' ')
        count+=1
    print()

#4
symbol = input()
all = "QWERTYUIOPASDFGHJKLZXCVBNM"
print('A'<=symbol<='Z' and "yes" or "no")
print(symbol in all and "yes" or "no")

#5
ls=[0,0,0,0,0,0,0,0]
count=0
for i in range (len(ls)):
    ls[i]=count
    count+=3
print(ls)

#6
# ls = [[0,0,0,0,0],
#       [0,0,0,0,0],
#       [0,0,0,0,0]]
a = int(input())
b = int(input())
if a>b: a,b=b,a
ls=[]

summa=0
for i in range(len(ls)):
    ls.append([])
    for j in range(5):
        ls[i].append(random.randint(a,b))
        # ls[i][j] = random.randint(a,b)
        summa+=ls[i][j]
print(ls)
print(f'avg: {summa/(len(ls)*len(ls[0]))}')


min=ls[0][0]
max=ls[0][0]
for i in ls:
    for j in i:
        if min>j:
            min=j
        if max<j:
            max=j
print(f"min: {min} max: {max}")

#8
def num_in_list(ls, num):
    for i in ls:
        if num==i:
            return True
    return False

#9
def all_even_nums(ls):
    result=[]
    for i in ls:
        if i%2:
            result.append(i)
    return result

#10
def get_column(ls, column_index):
    result=[]
    for i in ls:
        result.append(i[column_index])
    return result

#11
def all_numbers(st):
    result=[]
    ls = st.split(" ")
    for i in ls:
        if i.isdigit():
            result.append(i)
    return result

#12
student={
    "name": "Ivan",
    "group": "5A",
    "marks": []
}

journal=[]

def add_student():
    name = input("input name: ")
    group = input("input group: ")
    marks = input("input marks: ")
    student = {
        "name": name,
        "group": group,
        "marks": marks.split(" ")
    }
    journal.append(student)

def get_all_students_in_group():
    group = input("input group: ")
    result=[]
    for i in journal:
        if i["group"]==group:
            result.append(i)

def remote_student():
    name = input("input name: ")
    for i in range(len(journal)):
        if journal[i]["name"]==name:
            journal.pop(i)

def add_mark():
    name = input("input name: ")
    mark = input("input mark: ")
    for i in journal:
        if i["name"]==name:
            i["mark"].append(mark)

#отобразить всех студентов
def show_student():
    name = input("input name: ")
    for i in journal:
        if i["name"]==name:
            print(i)

def show_all():
    for i in journal:
        print(f"{i['name']} {i['group']}")

while True:
    variant = int(input(" 1 - add st, 2- remote st"))
    if variant==1: show_student()

ls = [2,3,2,5,3,54,4]

for i in range(len(ls)):
    print(ls[i])

for i in ls:
    print(i)

a=3

# if a>0:
#     print(0)
if a>4:
    print(1)
elif a>5:
    print(2)
# else:
#     print(3)


















