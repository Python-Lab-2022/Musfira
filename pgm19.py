list1=[]
list2=[]
n=int(input("enter the list of intergers: "))
print("enter the numbers: ")
for i in range(0,n):
    list1.append(int(input()))
print("The first integer list",list1)
list2=[i for i in list1 if i%2 !=0]
print("elements after removing even numbers: ",list2)

