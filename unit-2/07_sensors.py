# Sensor helpers for the mission console.
THRESHOLD = 70.0

# True when a reading exceeds the alert threshold.
def is_alert(value):
    return value > THRESHOLD

# Mean of a list of readings.
def average(values):
    return sum(values) / len(values)

# Run a self-test when the script is executed directly
if __name__ == "__main__":
    print("self-test:", is_alert(85), average([10, 20, 30]))