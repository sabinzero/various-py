code=input("give a integer (between 0 and 127) = ")
while(code < 0 or 127 < code):
    code=input("please try again")

print "for %d its %c" % (code,code)
