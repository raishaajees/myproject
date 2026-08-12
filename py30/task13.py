# Take a number as input and, using a loop, check whether it is a prime
#     number. Use break to stop checking as soon as you find a factor, and
#     print an appropriate message.

a=int(input("enter a number"))
i=2
while i<a:
    if a%i==0:
        print("the number is not prime")
    else:
        print("it is a prime number")
    break;  
