s = "ROBOTICS"

# string slicing
print(s[0], s[-1])
print(s[1:4])
print(s[:3], s[5:])
print(s[::-1])
print(len(s))


raw = " Alpha Rover "

# string methods
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().replace(" ", "_"))


packet = "T:25.4;H:60;B:78"

fields = packet.split(";")
print(fields)
for field in fields:
    key, value = field.split(":")
    print(key, "->", float(value))
print(";".join(fields))                 #prints every element of fields saparated by ";".