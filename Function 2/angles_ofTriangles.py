angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1 + angle2 + angle3 != 180 or angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print("Invalid triangle angles!")
else:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right Triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
