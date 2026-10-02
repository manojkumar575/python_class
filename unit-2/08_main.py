import importlib

# Dynamically import a module whose name starts with a number
sensors = importlib.import_module("07_sensors")

readings = [62, 84, 71]

# Access a constant and a function from the imported module
print("threshold:", sensors.THRESHOLD)
print("average :", sensors.average(readings))

# Evaluate each reading using a function from the imported module
for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")

# Inspect execution names for the current script and the imported module
print("__name__ inside main.py is:", __name__)
print("__name__ inside sensors is:", sensors.__name__)