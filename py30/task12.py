# Using a while loop, keep asking the user to enter numbers and keep adding
#     them to a running total, stopping only when the user types "stop".
#     Print the final total

total=0
while True:
    a=input("enter a num: ")
    if a.isdigit():
        a=int(a)
        total=total+a
        print(total)
    elif a=="stop":
        break
    else:
        print("enter only numbers")

