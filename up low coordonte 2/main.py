def inrectangle((rx0,ry0),(rx1,ry1),(x,y)):
    if rx0<x<rx1 and ry0<y<ry1:
        return True

x=input("get x: ")
y=input("get y: ")

myarea = (100,100)
if inrectangle((0,0),myarea,(x,y)) is not True:
    print "the point (%s,%s) is out of the area searched (%s,%s)" % (x, y, myarea[0], myarea[1])
    exit(10)

myrectagles=[
    [(0,0),(30,100)],
    [(30,0),(70,60)],
    [(50,60),(70,85)],
]

found = False
for i in myrectagles:
    if inrectangle(i[0],i[1],(x,y)) is True:
        print "the point (%s,%s) is in my area in %s" % (x,y,i)
        found = True
        break

if found is not True:
    print "the point (%s,%s) is not in my area" % (x,y)

