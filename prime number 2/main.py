from math import sqrt

i=2
c=0

n=input("enter a number : ")

sr=sqrt(n)

while i<=sr:
    r=n%i
    if r==0:
        c=1
        print "%d" % i

    i=i+1

if c==0:
    print "%d is a prime number" % n
else:
    print "%d is not a prime number" % n