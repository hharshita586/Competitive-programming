A = int(input("Enter a number: "))
if A % 5 == 0:
    if A % 11 == 0:
        print("The no is divisible by both 5 and 11")
    else:
        print("The no is not divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")
