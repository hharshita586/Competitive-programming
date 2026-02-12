# n = int(input("Enter a number: "))
# sum_n = 0
# for i in range(1, n + 1):
#     sum_n += i
# print("Sum:", sum_n)

#Make an assumption - Decide what your function does and trust that it will do it.
#Main logic - Solve a bigger problem using sub problem.
#Base case - When your recursion stop.



# def natural(n):
#     if n == 0:
#         return 0
#     return n + natural(n - 1)

# n = int(input("Enter a number: "))
# print("Sum:",natural(n))



# Using recursion print numbers from 1 to n.

# def print_num (n):
#     if n == 0:
#         return
#     print_num(n-1)
#     print(n)
# n = int(input())
# print_num(n)






# Using recursion print number from n to 1.
# Write a recursive function to find the nth fibonacci number.

# a= int(input("Enter a number: "))

# if (a & 1 == 0):
#     print("Odd")
# else:
#     print("Even")





# Given N array element, every element repeats twice except 1. find the unique element.

# A=[4, 1, 2, 1, 2]
# ans=0
# for i in range(len(A)):
#     ans=ans^ A[i]
# print(ans)


#Given N and i CHECK IF ith BIT IS set or NOT.

# n=int(input("enter number:"))
# i=int(input("Enter bit position: "))
# if ((n>>i)& 1==1):
#     print("set")
# else:
#     print("unset")




# given n count how many set bit are there in an array.

# arr=[2,6,8]
# Count=0
# for num in arr:
#     while num > 0:
#         Count += num & 1
#         num>>=1
# print("Count:",Count)


# x  b d y z z y d b d y z y d x