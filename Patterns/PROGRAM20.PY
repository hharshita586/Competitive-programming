# S= input()
# vowels= 'aeiouAEIOU'
# max_len=0
# current_len=0
# for char in S:
#     if char in vowels:
#         current_len +=1
#         max_len= max(max_len,current_len)
#     else:
#         current_len=0
# print(max_len)






# U have given a string "A" having upper case english letters u have to find how many times subsequence "AG" is there in a given string.
# "A B C G A G"

#Given N array elements,at every step remove an array element. Cost to remove element is equal to sum of array element present in it. Find minimum cost to remove elements.
# arr=[3,5,1,-3]
# s=sum(arr)
# cost=0
# for i in sorted(arr,reverse=True):
#     cost+=s
#     s-=i
# print(cost)





# # Given N array elements of unique number . calculate number of nobel integers present in the array.
# A[i]  is said to be nobel if ( number of elements less than A[i])=A[i]




#Given an integer array of A of size N return 1 if array can be arranged to form an AP otherwise return 0
def AP(A):
    A.sort()
    diff = A[1] - A[0]

    for i in range(1, len(A)-1):
        if A[i+1] - A[i] != diff:
            return 0

    return 1
A=[3,5,1]
print(AP(A))