def move_robot(x, y, speed=1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")

# Positional arguments (speed uses default 1.0)
move_robot(3, 4)

# Positional arguments with custom speed
move_robot(3, 4, 0.5)

# Keyword arguments (order doesn't matter)
move_robot(y=4, x=3)

# Mix of positional and keyword arguments
move_robot(3, speed=2.0, y=4)


# *values collects extra items into a tuple; **options collects named settings into a dictionary
def log(*values, **options):
    print("values :", values)
    print("options:", options)

log("start")
log("waypoint", 3, 4.5)
log("alert", level="high", retries=2)
log()