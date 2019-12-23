import math
a=input("enter quadratic equation factor: ")
b=input("enter quadratic equation factor: ")
c=input("enter quadratic equation factor: ")

d=pow(b,2)-4*a*c

if d<0:
    print "answer is complex number"
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    print "answer is %d and %d" %(x1,x2)