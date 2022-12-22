n = int(input("enter number of elements: "))
if n<= 0:
   print("Please enter a positive integer")
else:
    a=0
    b=1
    print(a)
    print(b)
for i in range(0,n-2):
    c=a+b
    print(c)
    a,b=b,c
    
