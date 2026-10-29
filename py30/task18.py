# Create a list of 5 numbers entered by the user (append them one by one
#     inside a loop). Then print the largest number, the smallest number, and
#     the sum of all numbers in the list (using loops and/or list methods,
#     not built-in max/min/sum).
a=int(input("num1:"))
b=int(input("num2:"))
c=int(input("num3:"))
d=int(input("num4:"))
e=int(input("num5:"))
yo=[]
yo.append(a)
yo.append(b)
yo.append(c)
yo.append(d)
yo.append(e)
print(yo)
for i in range (len(yo)):
    m=yo[0]
    for j in yo:
        if(j<m):
            m=j
            print(m)

