a=input("enter letter: ")
if ord(a)>=97 and ord(a)<=122:
    print "%c is letter" % (a)
else:
    if ord(a)>=65 and ord(a)<=90:
        print "%c is letter" % (a)
    else:
        print "%c isnt letter" % (a)
