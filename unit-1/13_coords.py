# Tuple creation
position = (5.4, 8.8)
print(position, type(position))

# Unpacking the tuple elements
x, y = position
print("x =", x, "| y =", y)

# Tuple with single element
single = (5,)
print(single, type(single))

# A set of visited elements without duplecates
visited = {(0, 0), (0, 1)}
visited.add((1, 1))
visited.add((0, 0))
print(visited)
print("count:", len(visited))
print("(1,1) visited?", (1, 1) in visited)      # Membership operator(in) checks whether the element
print("(9,9) visited?", (9, 9) in visited)      # is present in the set or no

# printing without duplecates
codes = ["E2", "E7", "E2", "E1", "E7"]
print("raw :", codes)
print("unique:", set(codes))
print("unique count:", len(set(codes)))
