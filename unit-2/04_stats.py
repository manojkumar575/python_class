def stats(values):
    return sum(values) / len(values), min(values), max(values)

readings = [22.5, 23.1, 21.8, 24.0, 22.9]

# Unpack the multiple values returned as a tuple
mean, lo, hi = stats(readings)
print(f"mean={mean:.2f} min={lo} max={hi}")

# Keep the result as a single tuple
packed = stats(readings)
print("as a tuple:", packed, type(packed))


def add_reading(data, value):
    data.append(value)  # Mutates the original list in place


def rebind(data):
    data = [99]  # Rebinds only the local variable name
    return data


# Modifying a mutable list changes it for the caller
readings1 = [10, 20]
add_reading(readings1, 30)
print("caller list is now:", readings1)

# Rebinding the local variable does not change the original list
readings2 = [10, 20]
rebind(readings2)
print("caller list unchanged:", readings2)