n = input("how many numbers: ")

numbers = []
for i in range(n):
    num = input("number[%d]: " % i)
    numbers.append(num)

print numbers
