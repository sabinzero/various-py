xc = input("enter how many numbers to sort: ")

rc = xc

print "enter %d numbers: " % xc

x = []
for i in range(xc):
    msg = "number[%d]: " % i
    a = input(msg)
    x.append(a)

r = []
for i in range(rc):
    r.append(0)

for i in range(xc):
    num = x[i]
    if i == 0:
        r[0] = num
        continue

    for j in range(0, i + 1):
        if num > r[j]:
            if j == i:
                r[j] = num
                break
            else:
                continue
        else:
            for k in range(i, j, -1):
                r[k] = r[k - 1]
            r[j] = num
            break

for i in range(rc):
    print "%d " % r[i]

print r
