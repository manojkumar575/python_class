#List methods: append, insert, remove, len, sorted

route = [(1, 1), (5, 1)]
print(route)

route.append((9, 3))
print("after append :", route)

route.insert(0, (0, 9))
print("after insert :", route)

route.remove((1, 1))
print("after remove :", route)

print(f"length: {len(route)} | sorted: {sorted(route)}")