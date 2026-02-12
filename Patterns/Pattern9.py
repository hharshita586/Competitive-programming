N = int(input("Enter number of rows: "))
for i in range(N):
    print("*" * (N - i), end="")
    print(" " * (2 * i), end="")
    print("*" * (N - i))
P