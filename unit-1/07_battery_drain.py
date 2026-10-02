battery = 100           # battery percentage
minutes = 0


# a loop to reduce battery percentage and to increase minutes
while (battery > 20):
    battery -= 7
    minutes +=1
    print(f"minute: {minutes:2d} -> battery: {battery}%")


# gives the low battery alert
print(f"Low-battery alert after {minutes} minutes ({battery}%)")