
#taking battery_cpt and current draw values from the user 
battery_cpt = float(input("Enter the battery capacity(mAh):")) 
current_draw = float((input("current draw(mA): ")))

#calculating and printing estimated runtime
runtime = battery_cpt/current_draw
print(f"Estimated runtime: {runtime:.2f}")