count = 0

def tick_shadow():
    # This creates a local variable 'count', shadowing the global 'count'
    count = 0
    count += 1
    return count

# Local 'count' resets each time; global 'count' remains 0
print(tick_shadow(), tick_shadow(), count)


THRESHOLD = 70

def is_alert(value):
    # Reading a global variable or constant works fine without any special keyword
    return value > THRESHOLD

print(is_alert(85), is_alert(60))


counter = 0

def tick_global():
    # The 'global' keyword allows modifying the outer variable
    global counter
    counter += 1
    return counter

print(tick_global(), tick_global(), tick_global())
print("global counter is now:", counter)


def tick(n):
    return n + 1

# Best practice approach: pass data in and assign the returned value out
total = 0
total = tick(total)
total = tick(total)
print("total:", total)