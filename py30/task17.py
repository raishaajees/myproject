# Take a sentence as input and count how many vowels (a, e, i, o, u) it
#     contains using a loop and string membership checks. Also use a
#     validation method (like isalpha() or isdigit()) to check whether a
#     separate user-entered value is purely alphabetic or purely numeric.

# sen=input("enter a sentence: ")
# count=0
# val={}
# val[]
# v=["a","e","i","0","u"]
# if sen.isdigit():
#     print("enter only sentence")
# for i in v:
#          if sen.isalpha() or " " in sen:
#              if (i in sen):
#                   print(i)
#                   count=count+1
#                   print(count)


sen=input("enter a sentence: ")
a=sen.lower()
v=["a","e","i","o","u"]
emp={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in a:
    if i in v:
        emp[i]+=1
print(emp)




