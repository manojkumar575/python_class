#operators 
print(17 / 5)                # normal division returns quotient
print(17 // 5)               # floor division 
print(17 % 5)                # prints remainder
print(2 ** 10)               # prints 2^10
print(-17 // 5)              # Rounds down to the lower integer


print("compass:", (359 + 2) % 360)    #always prints positive number
print("negative:", (-30) % 360)


distance = 8.0
limit = 10.0
battery = 45


# relational and logical operators
print(distance < limit)
print(distance == limit)
print(0 <= distance < limit)
print(distance > 5 and battery > 20)
print(distance > 5 or battery > 90)
print(not (distance > 5))