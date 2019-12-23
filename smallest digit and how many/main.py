n = input("enter number: ")

a = n
i = 0
while a != 0:
    a /= 10
    i += 1
print "the number %d has %d digits" % (n,i)

a = n
minim = a % 10

while a != 0:
    a /= 10
    last_digit = a % 10

    if last_digit <= minim and last_digit != 0:
        minim = last_digit

print "smallest digit is: %d" % minim
