import math
import random
from datetime import datetime, timedelta

# Perform basic math calculations
print(math.sqrt(16))
print(math.hypot(3, 4))
print(round(math.pi, 4))
print(math.factorial(5))
print(math.degrees(math.pi / 2))

# Generate pseudo-random numbers with a fixed seed for reproducibility
random.seed(42)
print(random.randint(1, 100))
print(round(random.uniform(20.0, 30.0), 2))
print(random.choice(["Alpha", "Beta", "Gamma"]))

# Simulate noisy sensor readings using a Gaussian distribution
noisy = [round(25 + random.gauss(0, 0.5), 2) for _ in range(5)]
print("simulated sensor:", noisy)

# Manage timestamps and calculate time intervals
start = datetime(2026, 9, 4, 9, 30, 0)
end = start + timedelta(minutes=42)
print("start:", start.strftime("%d-%m-%Y %H:%M"))
print("end :", end.strftime("%d-%m-%Y %H:%M"))
print("duration:", (end - start).total_seconds() / 60, "minutes")