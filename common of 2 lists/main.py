print "enter first list of numbers ('end' to stop)"
a=[]
numb=input("next: ")
while numb!="end":
    a.append(numb)
    numb = input("next: ")
ac=len(a)

print a

print "enter second list of numbers ('end' to stop)"
b=[]
numb=input("next: ")
while numb!="end":
    b.append(numb)
    numb = input("next: ")
bc=len(b)

print b

res=[]
for i in range(ac):
    for j in range(bc):
        if a[i]==b[j]:
            res.append(b[j])
rc=len(res)

print "%d common elements: " % (rc)

print res


