fac = 1

n = input("factorial of: ")

for i in range(1, n + 1):
    fac *= i

print "factorial of %d is: %d" % (n, fac)
