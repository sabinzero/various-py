a = input("enter number a: ")
b = input("enter number b: ")

k = 0
j = 0
even = []
odd = []

if a < b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
else:
    for i in range(a, b - 1, -1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

print even

print odd
