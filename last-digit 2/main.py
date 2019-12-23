from math import ceil

a=input("get number: ")

n=a/10.0
print "n= %f" % n

f=int(n)
print "f= %d" % f

x=ceil((n-f)*10)

print "x= %f" % x