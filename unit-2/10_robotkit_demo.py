import importlib

sensors = importlib.import_module("09_robotkit.sensors")
control = importlib.import_module("09_robotkit.control")


d = sensors.read_ultrasonic()
print("distance:", d, "->", control.decide(d))
print("package contents:", [n for n in dir(control) if not n.startswith("_")])