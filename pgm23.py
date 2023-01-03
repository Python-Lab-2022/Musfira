import math
a=int(input("Enter the starting index:"))
b=int(input("Enter the ending index:"))
if(a<=1000,b>=10000):
    print("enter 4 digit number")
else:
    for i in range(a,b):
        n=int(math.sqrt(i))
        if(n*n==i):
            n=i
            while(n!=0):
                r=n%10
                n=n//10
                if(r%2!=0):
                    break
                else:
                    print(i)
            

