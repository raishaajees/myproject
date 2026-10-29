# Create a list of 5 numbers entered by the user (append them one by one
#     inside a loop). Then print the largest number, the smallest number, and
#     the sum of all numbers in the list (using loops and/or list methods,
#     not built-in max/min/sum).

n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
num=[]
num.append(n1)
num.append(n2)
num.append(n3)
num.append(n4)
num.append(n5)
print(num)
for i in range(len(num)+1):
    m=num[0]
    for j in num:
        if j>m:
            m=j
print("the greatest num is:",m)

for i in range(len(num)+1):
    m=num[0]
    for j in num:
        if j<m:
            m=j
print("the smallest num is:",m)

total=0
for i in num:
    total+=i
print(total)