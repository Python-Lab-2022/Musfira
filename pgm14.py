list1 = []
list2 = []
a = int(input("enter no of colors "))
print("first list of colors ")
for i in range(0,a):
    list1.append(str(input()))
print("first list is : ",list1)
b = int(input("enter no of colors "))
print("second list of colors ")
for i in range(0,b):
    list2.append(str(input()))
print("second list is : ",list2)
print("\nDifferenct of list1 and list2:")
print(list1.difference(list2))
print("\nDifferenct of list2 and list1:")
print(list2.difference(list1))
