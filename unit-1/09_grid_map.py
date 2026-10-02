obstacles = [(1, 2), (3, 3), (0, 4)]  # coordinates of the obsticles

# checks for the obsticles. if obsticle is detected then prints "#" else prints ".".
for row in range(5):
    for col in range(5):
        if (row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end="")
    print()

# caculating sum, count and mean of this list
readings = [22.5, 23.1, 21.8, 24.0, 22.9]

total = 0
for r in readings:
    total += r

print("sum :", total)
print("count :", len(readings))
print("mean :", total / len(readings))

# checks for the values which are above 70. if none of the values are above 70 then else block is executed
checks = [12, -1, 34, 78, 15]
for r in checks:
    if r < 0:
        continue
    if r > 70:
        print("DANGER at", r)
        break
else:
    print("all readings safe")