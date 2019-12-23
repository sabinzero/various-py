a=input("enter number: ")

while a<10 or a>99:
    print "number must have 2 digits"
    a = input("enter number: ")

if a%2==0:
    s = a/10 + a%10
    print "sum of digits is : %d" % s
else:
    d = a/10 - a%10
    print "difference of digits is : %d" % d


