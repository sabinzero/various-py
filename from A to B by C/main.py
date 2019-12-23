start=input("from ")
end=input("to ")

while start==end:
    print "numbers cant be equal"

    start = input("from ")
    end = input("to ")

step=input("step by ")

if(start<end):
    for i in range(start,end+1,step):
        print "%d" % (i)
else:
    for i in range(start,end-1,-step):
        print "%d" % (i)