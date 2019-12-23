a=input("first number: ")
b=input("second number: ")

if a>b:
    print "%d is bigger than %d" % (a,b)
else:
    if a<b:
        print "%d is bigger than %d" % (b,a)
    else:
        print "%d is equal to %d" % (a, b)