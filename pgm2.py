list = []
a = int(input("enter size of list "))
print("enter element of list")
for i in range(0,a):
    e = int(input())
    list.append(e)
    
print("positive numbers in list are: ")
for i in list:
    if i>=0:
        print(i)
#b
print("square are: ")
for i in list:
    print(i*i)

#c

string = input("enter a string")
vowels = "AaEeIiOoUu"
final = [i for i in string if  i in vowels]
print("no of vowels in the string is")
print(len(final))
print(final)


#d
string = input("enter a word")
for char in string:
    print(char,'-',ord(char))
