# Movement decisions for robotkit.
from . import sensors as _sensors


# Return STOP, SLOW or GO for a distance in centimetres.
def decide(distance):
    if distance < _sensors.STOP_CM:
        return "STOP"
    elif distance < _sensors.SLOW_CM:
        return "SLOW"
    return "GO"