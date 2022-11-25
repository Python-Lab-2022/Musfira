list = []
n = int(input("enter no of colors: "))
print("colors are: ")
for i in range(0,n):
    list.append(str(input()))
print(list)
print("The first element of the list : ",list[0])
print("The last element of the list : ",list[-1])
