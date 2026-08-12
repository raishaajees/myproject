# Print the multiplication table of a number entered by the user, from 1 to
#     10, using a for loop.

a=int(input("enter a num: "))
for i in range(1,11):
    print(f"{i}*{a}={i*a}")