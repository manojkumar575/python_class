# uses a mutable list [] as a default argument
def add_waypoint(wp, route=[]):
    route.append(wp)
    return route

r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))

print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)  # True! They share the exact same list.


# uses None to create a fresh list every time
def add_waypoint_fixed(wp, route=None):
    if route is None:
        route = []  # Creates a new list on each call
    route.append(wp)
    return route

r1 = add_waypoint_fixed((0, 0))
r2 = add_waypoint_fixed((5, 5))

print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)  # False! They are separate lists.