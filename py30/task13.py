# Take a number as input and, using a loop, check whether it is a prime
#     number. Use break to stop checking as soon as you find a factor, and
#     print an appropriate message.



while True:
    user = input("Enter a Valid whole number: ")
    if user.isdigit():
        user = int(user)
        print(f"You entered {user}.")
        break
    else:
        print("Enter a numeric value only! idiot")



if user < 2:
    print(f"{user} is not a prime number")
elif user == 2:
    print(f"{user} is a prime number")
elif user % 2 == 0:
    print(f"{user} is not a prime number")
else:
    # root = int(user ** 0.5)
    prime = True
    for i in range(3,user+1,2):
        if user % i == 0:
            print(f"{user} is not a prime number")
            prime = False

    if prime:
        print(f"{user} is a prime number")
