# Take a list of numbers and create a new list containing only the even
#     numbers from it, using a for loop and the append() method.

num=[1,2,3,4,5,6,7,8,9,10]
li=[]
for i in num:
    if i%2==0:
        li.append(i)
print(li)