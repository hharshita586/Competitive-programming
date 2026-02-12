#You are provided with an integer array A. Return another array B of size same as that of
#A such that B[i] = A[i]^3
#Input:
#A=[2, 6, 8, 1]
#Output:
#[8, 216, 512, 1]

a=list(map(int,input().split()))
b=int(input())
result=[]
for i in a:
    result.append(i**b)
print(result)