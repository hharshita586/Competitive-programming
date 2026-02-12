num = int(input("Enter a positive number: "))
if num > 0:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i)
        i += 1
else:
    print("Enter a positive number")
