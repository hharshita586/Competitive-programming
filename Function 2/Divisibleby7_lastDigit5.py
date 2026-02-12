n = int(input("Enter a number: "))

if n % 7 == 0:
    print("Yes")
else:
    if n % 10 == 5:
        print("Yes")
    else:
        print("No")


