x_pos = 1.0             #robot x-coordinate
robot_name = "alpha"    #robot name
is_docked = False       
battery_pct = 45       #battery percentage

#prints the robot details 
print(f"x-position: {x_pos} it is of type: {type(x_pos)}")
print(f"robot name: {robot_name} it is of type: {type(robot_name)}")
print(f"is docked: {is_docked} it is of type: {type(is_docked)}")
print(f"battery percentage: {battery_pct} it is of type: {type(battery_pct)}")

#condition that checks whether the robot's battery percentage is less than 50 or not
if(battery_pct<50):
    print("Charging recommended")
    print("Docking now..")