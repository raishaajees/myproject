# Ask the user to enter three values on separate input() calls, use type()
#    to check and print the datatype of each entered value before and after
#    converting it to int and float, and explain (as a comment) why input()
#    always returns a string.

a=input("enter first value: ")
b=input("enter second value: ")
c=input("enter third value:")
inputs=[a,b,c]
for i in inputs:
    if i.isdigit():
        print(f"the {i} is {type(i)}")
        i=int(i)
        print(type(i))
        i=float(i)
        print(type(i))

    else:
         print(f"the {i} is {type(i)}")

#  input function returns user input as strings
       

  
