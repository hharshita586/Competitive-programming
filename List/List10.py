# Given an array A, Find the reverse of it. (Solve this question with for loop)
#Input:
#A =[3, 5, 1, 2, 1, 2]
#Output:
#[2, 1, 2, 1, 5, 3]

a = list(map(int, input().split()))
result = []

for i in a:
    result.insert(0, i)
print(result)