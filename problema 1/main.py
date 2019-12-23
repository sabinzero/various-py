n = 30
k = 2
i = 1

while i <= n / 4:
    print "%d " % k
    k += 1
    k = n / k + n % k
    i += 1
