# Create two sets of numbers from user input (5 numbers each, allow
#     duplicates while entering). Print the union, intersection, and
#     difference of the two sets, and also print whether the first set is a
#     subset of the second.

list1=[]
list2=[]

count=0
while count<5:
    set1=int(input("enter num: "))
    count+=1
    list1.append(set1)
print(list1)
s1=set(list1)
print(s1)

count=0
while count<5:
    set2=int(input("enter num: "))
    count+=1
    list2.append(set2)
print(list2)
s2=set(list2)
print(s2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.issubset(s1))

