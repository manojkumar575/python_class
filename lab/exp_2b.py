# find the largest number

num1 = eval(input("Enter the value of num1: "))
num2 = eval(input("Enter the value of num2: "))
num3 = eval(input("Enter the value of num3: "))
num4 = eval(input("Enter the value of num4: "))
num5 = eval(input("Enter the value of num5: "))

if (num1 > num2) and (num1 > num3) and (num1 > num4) and (num1 > num5):
    print(f"Largest number is {num1}")

elif (num2 > num1) and (num2 > num3) and (num2 > num4) and (num2 > num5):
    print(f"Largest number is {num2}")

elif (num3 > num1) and (num3 > num2) and (num3 > num4) and (num3 > num5):
    print(f"Largest number is {num3}")

elif (num4 > num1) and (num4 > num2) and (num4 > num3) and (num4 > num5):
    print(f"Largest number is {num4}")

elif (num5 > num1) and (num5 > num2) and (num5 > num3) and (num5 > num4):
    print(f"Largest number is {num5}")