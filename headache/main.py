fact = 1
sum = 0

n = input("enter value of n: ")

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += fact
    print "%d! = %d" % (i, fact)

print "sum of factorial of every individual number is : %d" % (sum)
