# Take a year as input and print whether it is a leap year or not (a year is
#    a leap year if it is divisible by 4, but century years must also be
#    divisible by 400).

year=int(input("enter a year: "))
if year%4==0:
    if year%400==0:
        print(f"The year {year} is a leap year")
else:
    print(f"The given year is not a leap year")

