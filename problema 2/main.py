n = input("how many numbers: ")

for i in range(1, n + 1):
    num = input("number: ")

    if i == 1:
        minp = num

    if 0 < num and num < minp:
        minp = num

print "smallest positive number: %d" % (minp)
