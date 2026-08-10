# Take a user's name and age as input (age entered as text), convert age to an integer using type casting, and print a message like: "Hi , in 5 years you will be <age+5> years old."
def task():
    name=input("enter ur name: ")
    while True:
        age=input("enter ur age:")
        if age.isdigit():
            age = int(age)
            print(f"hi {name} in 5 years you will be{age+5} years old")
            break
    return name, age
task()

