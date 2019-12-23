x=input("enter x: ")
y=input("enter y: ")

areax=100
areay=100

if x>100 or y>100 or x<0 or y<0:
    while x>100 or y>100 or x<0 or y<0:
        print "wrong input, try again!"
        x = input("enter x: ")
        y = input("enter y: ")
else:
    if 0<=x<=30 and 0<=y<=100:
        print "its low"
    else:
        if 30<=x<=70 and 30<=y<=60:
            print "its low"
        else:
            print "its up"
