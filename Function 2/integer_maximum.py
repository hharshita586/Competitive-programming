a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print("The maximum number is:", maximum)
