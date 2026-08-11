# #Take the length and breadth of a rectangle as input. Using arithmetic
#    operators, print its area and perimeter. Then use the modulo operator to
#    check and print whether the area is an even or odd number.

length=int(input("enter the length of rectangle: "))
breadth=int(input("enter the breadth of rectangle: "))
area=length*breadth
perimeter=2*(length+breadth)
print("area of rectangle is ",length*breadth)
print("perimeter of rectangle is ",2*(length+breadth))
if area%2==0:
    print("area is even")
else:
    print("area is odd")      
