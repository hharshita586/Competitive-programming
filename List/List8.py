#YouareprovidedwithanintegerarrayA.ReturnanotherarrayBofsizesameasthatof
#AsuchthatB[i]=A[i]^2
#Input:
#A=[2,6,8,1]
#Output:
#[4,36,64,1]

a=list(map(int,input().split()))
b=int(input())
result=[]
for i in a:
    result.append(i**b)
print(result)