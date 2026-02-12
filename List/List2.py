#Copy the Array
#You are given a constant array A and an integer B.
#You are required to return another array where Arr[i] = A[i] + B.

a=list(map(int,input().split()))
b=int(input())
result=[]
for i in a:
    result.append(i+b)
print(result)
