# Take a sentence as input and count how many vowels (a, e, i, o, u) it
#     contains using a loop and string membership checks. Also use a
#     validation method (like isalpha() or isdigit()) to check whether a
#     separate user-entered value is purely alphabetic or purely numeric.

sen=input("enter a sentence: ")
count=0
v=["a","e","i","0","u"]
if sen.isdigit():
    print("enter only sentence")
if sen.isalpha():
    for i in v:
        if (i in sen):
            count=count+1
    print(count)