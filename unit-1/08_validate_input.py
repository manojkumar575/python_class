
# input validation
while True:
 text = input("Enter battery % (0-100): ")
 value = float(text)
 if 0 <= value <= 100:
    break
    print("out of range, try again")
print("accepted:", value)                  #prints the accepted value