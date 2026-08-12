# Rebuild the "grading system" style program from your Control Flow notes:
#    take marks (0-100) as input and print a grade (A+, A, B, C, D, or Fail)
#    based on ranges of your choice using if / elif / else. Validate that the
#    input is a number using isdigit() before grading it.

name=input("enter ur name: ")
while True:
    marks=input("enter ur marks:")
    if marks.isdigit():
        marks=int(marks)
    else:
        print(input("enter only digits "))
    break;
if marks>90:
      print("A+")
elif marks>80:
      print("A")
elif marks>70:
     print("B")
elif marks>40:
     print("C")
elif marks<40:
     print("fail")
    

    






