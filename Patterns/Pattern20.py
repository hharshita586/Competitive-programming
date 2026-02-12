##reverse the order of the words
##string=" python programming"

string = " python programming"
print(' '.join(string.split()[::-1]))



#reverse each word individually in a string
#like PROGRAM - MARGORP

string = "PROGRAM PYTHON"
print(' '.join(word[::-1] for word in string.split()))


