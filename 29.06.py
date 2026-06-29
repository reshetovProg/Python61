# a = 678
# b = str(a)
# print(int(b[2]+b[1]+b[0])*2)

#
# for i in data:
#     print(i,end=" ")

# marks = [2,3,-4,7,6,4,6,8,9]
# print(marks)
# for i in range (len(marks)//2):
#     marks[i], marks[len(marks) - (i+1)] = marks[len(marks) - (i+1)], marks[i]
# print(marks)
# for i in marks:
#     if i<0:
#         print(i,end=" ")
#
# for i in range (len(marks)):
#     if marks[i]<0:
#         marks[i]*=-1


#
# a = 7
# print(a)
#
# b = "Вася"
# print(b)
#
# a = [1,2]
# print(a[0])
# b = ["Вася", "Петя"]
# print(b[0])








# students = ["Иван", "Максим", "Ива", "Ольга"]
#
# for i in students:
#     if i[len(i)-1]=="а":
#         print(i,end=" ")
# print()
# for i in range (len(students)):
#     if students[i][len(students[i])-1]=="а":
#         print(students[i],end=" ")

# flag = True
# for i in range (1, len(student)):
#     if len(student[i])!=len(student[0]):
#         flag=False
#         break
# print(flag and "все равны" or "разные")
#
# for i in range (len(marks)):
#     if marks[i]%2==0:
#         marks[i]+=1
#     print(marks[i], end=" ")
# print()
# print(marks)
#
# for i in marks:
#     if i%2==0:
#         i+=1
#     print(i,end=" ")
# print()
# print(marks)

students = [[2,3,4,3],
            [3,4,3,5],
            [4,4,4,5]]


print(students[1][len(students[1])-1])

for i in range (len(students)):
    summa=0
    for j in students[i]:
        summa+=j
        print(j,end="\t")
    print("|",summa)
print("--------------")
result = 0
for i in range(len(students[0])):
    summa=0
    for j in range(len(students)):
        summa+=students[j][i]
    print(summa, end="\t")
    result+=summa
print("|",result)


sp = [[2,3,4],
      [3,1,7]]

for i in range(len(sp)):
    summa = 0
    for j in sp[i]:
        summa += j
        print(j,end=" ")
    print("=",summa)
result = 0
for i in range(len(sp[0])):
    total = 0
    for j in range (len(sp)):
        total += sp[j][i]
    result += total
    print(total,end=" ")
print("=",result)
