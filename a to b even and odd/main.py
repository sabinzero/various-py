a=input("enter number a: ")
b=input("enter number b: ")

if a<b:
    for i in range(a,b+1):
        if i%2==0:
            print i
    print "---"
    for i in range(a,b+1):
        if i%2!=0:
            print i
else:
    for i in range(a,b-1,-1):
        if i%2==0:
            print i
    print "---"
    for i in range(a,b-1,-1):
        if i%2!=0:
            print i