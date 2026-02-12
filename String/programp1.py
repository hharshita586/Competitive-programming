#u have given a string "S". U have to find all amazing substring of S. And amazing substring is one that start with a vowel.

# S = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for i in range(len(S)):
#     if S[i] in vowels:
#         count += (len(S) - i)
# print(count)






#Find the number of "bob" in string A consisting of lower case english alphabates.

# A = input("Enter a string: ")
# count = 0
# for i in range(len(A) - 2):
#     if A[i:i+3] == "bob":
#         count += 1
# print(count)






# Print all subarray of given array . A= [1 , 2 ,3]
# A = [1, 2, 3]
# for i in range(len(A)):
#     for j in range(i, len(A)):
#         print(A[i:j+1])






# Print sum of every single subarray. A= [1 , 2 ,3]

# A = [1, 2, 3]
# for i in range(len(A)):
#     sum_sub = 0
#     for j in range(i, len(A)):
#         sum_sub += A[j]
#         print(f"Subarray {A[i:j+1]} -> Sum = {sum_sub}")






# Given an integer array "nums". find the subarray with their largest sum.
# -2 , 1, -3, 4, -1, 2, 1, -5, 4


#Given an array fined the sum of all subarray sum.



# Given an array A of N non-negative numbers and a non-negative number B, you need to find the number of subarrays in A  whose sum will be less than B.


# A = [2, 5, 6]
# B = 10
# n = len(A)
# count = 0

# for i in range(n):
#     curr_sum = 0
#     for j in range(i, n):
#         curr_sum += A[j]
#         if curr_sum < B:
#             count += 1
#         else:
#             break
# print(count)



#Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. LENGTH OF THE SUBARRAY IS BE EVEN,  AND THE SUM OF ALL THE ELEMENTS OF THE SUBARRAY MUST BE LESS THAN B
# 2. LENGTH OF THE SUBARRAY IS BE ODD, AND THE SUM OF ALL THE ELEMENTS OF THE SUBARRAY MUST BE GREATER THAN B.
# your task is to find the count of good subarrays in A.

# A=[2,5,6]
# B=10
# count=0
# N=len(A)
# for i in range(N):
#     sum=0
#     for j in range(i,N):
#         sum+=A[j]
#         length=j-i+1
#         if length%2==0 and sum <B:
#             count+=1
#         if length%2==1 and sum >B:
#             count+=1
# print(count)



# [11, 12, 13, 14, 15]

# You have given an integer array C of size A.
# Now you need to find a subarray(contiguous elements)so thaht the sum of contiguous elements is maximum. but the sum must not be exceed B.
# A=5
# b=12
# c=[2, 1, 3, 4, 5]

# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]
# max_sum = 0

# for i in range(A):
#     curr_sum = 0
#     for j in range(i, A):
#         curr_sum += C[j]
#         if curr_sum <= B and curr_sum > max_sum:
#             max_sum = curr_sum
# print(max_sum)



# GIVEN AN ARRAY OF A LENGTH N .YOUR TASK IS TO FIND MAXIMUM POSSIBLE SUM OF ANY NON-EMPTY CONTINUOUS SUBARRAY IN OTHER WORDS ALL POSSIBLE SUBARRAYS OF A DETERMINE AMONG THE ONE THAT REACHES THE HIGHEST SUM


A=[2, 5, 6]
max_sum=A[0]
current_sum=0
for i in range(len(A)):
    current_sum+=A[i]
    if current_sum>max_sum:
        max_sum=current_sum
    if current_sum<0:
        current_sum=0
print(max_sum)

