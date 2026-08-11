# # Take a single number as input. Using comparison and logical operators
#    (and / or), print True or False for each of the following in one line each:
#    whether it is positive AND even, whether it is negative OR zero, and
#    whether it is divisible by both 3 and 5.
a=int(input("enter a number: "))
if a>0 and a%2==0:
    print("true")
else:
    print("false")
if a<0 or a==0:
    print("true")
else:
    print("false")
if a%3==0 and a%5==0:
    print("true")
else:
    print("false")



