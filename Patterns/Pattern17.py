N= int(input())
for i in range(N):
    for j in range(1,N-i+1):
        print(j,end=" ")
    for k in range(2 * i -1):
        print("*",end=" ")
    print()