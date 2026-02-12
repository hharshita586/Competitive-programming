per = float(input("Enter percentage: "))

if per >= 90:
    grade = "A+"
elif per >= 80:
    grade = "A"
elif per >= 70:
    grade = "B"
elif per >= 60:
    grade = "C"
elif per >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
