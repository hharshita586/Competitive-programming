N = int(input("Enter rows: "))
for i in range(N):
    for j in range(N):
        if j<i:
            print("_", end=" ")
        else:
            print("*", end=" ")
    print()
