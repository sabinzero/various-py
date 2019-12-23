n = input("how many elements: ")

a = []
for i in range(n):
    b = input("give number[%d]: " % i)
    a.append(str(b))

print a

print " ".join(a)
print " ".join(a)

for i in range(n):
    print "%s" % a[i]
