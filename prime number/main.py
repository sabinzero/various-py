from math import sqrt

num = input("enter number: ")

x = int(sqrt(num))

for i in range(2, x + 1):
    if num % i == 0:
        print "number is not prime"
        exit(0)

print "number is prime"
