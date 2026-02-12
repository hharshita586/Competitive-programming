#Max and Min of an Array
# Take input an array A of size N and write a program to print maximum and minimum
#elements of the input array .Here N represents the length of the array .

a = list(map(int, input().split()))
max=a[0]
min=a[0]
for i in a :
    if i>max:
        max =i
    elif i<min:
        min=i
print(max)
print(min)