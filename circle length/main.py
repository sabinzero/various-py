PI=3.1415926

r=input("get radius: ")

while r<0:
    print "radius cannot be negative"
    r=input("get radius: ")

circle_len = 2 * PI * r
"circle_length = %f" % circle_len