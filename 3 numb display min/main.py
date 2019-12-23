a=input("enter number: ")
b=input("enter number: ")
c=input("enter number: ")

if a<b and a<c:
    print "%d is min" % a
else:
    if b<a and b<c:
        print "%d is min" % b
    else:
        if c<a and c<b:
            print "%d is min" % c