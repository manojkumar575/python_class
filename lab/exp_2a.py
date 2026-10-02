# Triangle classification

s1 = eval(input("Enter the length of side 1: "))
s2 = eval(input("Enter the length of side 2: "))
s3 = eval(input("Enter the length of side 3: "))

if(s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("It is a valid Triangle")
    if (s1 == s3):
        print("It is an Equilateral Triangle")

    elif (s1 == s2) or (s1 == s3) or (s2 == s3):
        print("It is an isosceles Triangle")

    else:
        print("It is a Scalene Triangle")

else:
    print("It is not a Triangle")