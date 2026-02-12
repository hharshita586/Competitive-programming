# Given two lists A1 and A2, each containing integers, write a Python program to compute
#the element-wise sum of the corresponding elements in the two lists and store the result
#in a new list.

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)