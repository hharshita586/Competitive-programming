N = int(input("Enter rows: "))
for i in range(1, N+1):
    for j in range(1, N+1):
        if j <= N-i:
            print("_", end="")
        else:
            print("*", end="")
    print()
