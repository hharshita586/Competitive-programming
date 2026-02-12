N=int(input("enter rows: "))
for i in range(N):
    for j in range(N):
        if j==0 or j== N-1:
            print("*", end= " ")
        else:
            print("_", end=" ")
    print()