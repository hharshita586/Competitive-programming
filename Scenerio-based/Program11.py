#given a string. calculate the length of longest palindromic substring.
# for every substring check if it a palindrome or not and get the maximum length.


def longest_palindrome_length(s):
    n=len(s)
    s=input()
    max_length=1
    for i in range(0,n):
        for j in range(i,n):
            is_palindrome=True

