THRESHOLD = 70.0    # Threshold value 
readings = []

# keep the program on loop untill it hits break statement.
while True:
     # get the choice from the user.
    print("\n1-add reading 2-report 3-quit")     
    choice = input("choice: ")

    # if choice is 1 then take the value form the user and store it in readings
    if choice == "1":
        value = float(input("sensor value: "))
        readings.append(value)
    
    #if choice is 2 print the report.
    elif choice == "2":
        if not readings:
            print("no data yet")
            continue

        alerts = 0
        for r in readings:
            if r > THRESHOLD:
                alerts += 1
        avg = sum(readings) / len(readings)
        print(f"count={len(readings)} avg={avg:.1f} alerts={alerts}")

    # if choice is 3 stop the program.
    elif choice == "3":
        print("mission console closed")
        break

    # if choice is other than 1, 2, and 3 print invalid choice.
    else:
        print("invalid choice")
