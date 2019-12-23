a=5
b=4
c='d'
c+=b
c+=1
print "%d" % c
print "%d" % b
b+=1

a=2
b+=a

print "%d" % (++b)
print "%d" % (++b)
print "%d" % c

print "%d" % (a++)
print "%d" % (b++)
print "%d" % (c++)

print "%d" % (++a)
print "%d" % (++c)
print "%d" % (++b)

c-=-3

print "%d" % (++b)
print "%d" % (++c)
print "%d" % (++a)