N = int(input("Enter rows: "))
for i in range(N):
    if i == N-1:
        print(("*_*"))
    else:
        print("*" + "_" * (N-i-0) + "*")
