#Search Element
#You are given array A and an integer B. You have to tell whether B is present in array A
#or not.

a = list(map(int, input().split()))
b=int(input())

if b in a:
    print("1")
else:
    print("2")