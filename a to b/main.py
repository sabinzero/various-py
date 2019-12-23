a = input("enter number a: ")
b = input("enter number b: ")

if a < b:
    for i in range(a,b+1):
        print i
else:
    for i in range(a,b-1,-1):
        print i
