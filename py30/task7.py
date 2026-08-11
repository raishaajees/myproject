# Take three numbers as input and print the largest of the three using
#    nested if statements.

a=int(input("enter num1: "))
b=int(input("enter num2: "))
c=int(input("enter num3: "))

if a > b:
    if a > c:
        print(f"{a} is bigger than {b} {c}")
    else:
        print(f"{c} is bigger than {a} and {b}")
else:
    if b > c:
        print(f"{b} is bigger than {a} {c}")
    else:
        print(f"{c} is bigger than {a} and {b}")







# if a>(b and c):
#     print("a is greater")
#     if b>(a and c):
#         print("b is greater")
#         if c>(a and b):
#             print("c is greater")