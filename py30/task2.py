# Take two numbers as input from the user (they will come in as strings),
#    type-cast them to int, and print their sum, difference, product, and
#    quotient. Use print() with multiple arguments in one line for each result.

while True:
    a=input("enter first number")
    if a.isdigit():
        a=int(a)
        break
    else:
        print("enter only digit")
    


while True:
    b=input("enter second number")
    if b.isdigit():
        b=int(b)
        break
    else:
        print("enter only digit")
    

print(a+b,a-b,a*b,a/b)