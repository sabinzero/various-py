p = 1

n = input("enter how many numbers: ")

for i in range(n):
    num = input("number[%d]: " % i)

    if num != 0:
        p *= num

print "the product of number without 0 is: %d" % p
