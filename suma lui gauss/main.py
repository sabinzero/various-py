n = input("enter number: ")

sg = 0
for i in range(1, n + 1):
    sg += i

print "sum of numbers from 1 to %d is: %d" % (n, sg)
