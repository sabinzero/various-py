from math import sqrt


def prime(n):
    res = 1
    x = int(sqrt(n))
    for i in range(2, x + 1):
        if n % i == 0:
            return 0
    return res


num1 = input("enter first number: ")
num2 = input("enter second number: ")

a = num1 + 1 if num1 % 2 == 0 else num1 + 2
b = num2 - 1 if num2 % 2 == 0 else num2 - 2

iterat = 0
prm = []
for i in range(a, b + 1, 2):
    if prime(i) == 1:
        prm.append(i)
    iterat += 1

k = len(prm)
print "the number of primes between %d and %d is: %d" % (num1, num2, k)
print "the number of iterations: %d" % iterat
print prm
