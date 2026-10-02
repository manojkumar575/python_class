robot = {"name": "Alpha", "battery": 78, "mode": "auto"}


print(robot)                    # prints complete dictionary.
print(robot["name"])            # prints the value of "name".

robot["battery"] -= 2           # updates teh battery value.
robot["speed"] = 0.8            # creates a new key value pair as speed is not present.
print(robot)

print(robot.get("current"))     # .get method is used to get the value safely. if not found returns none.
print(robot.get("current", 0.0)) # if "current" is not found it returns 0.0 .
print("speed" in robot)

log = ["E2", "E7", "E2", "E1", "E7", "E2"]

# creates a new empty dictionary and stores the key and its frequency.
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)

# prints the key value pairs of freq
for code in sorted(freq, key=freq.get, reverse=True):
    print(f"{code} occurred {freq[code]} time(s)")

#prints the key value pairs of robot
for key, value in robot.items():
    print(f"{key:<8} {value}")
