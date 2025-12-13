
# laptop battery check code


import psutil

battery = psutil.sensors_battery()

print("Battery Persantage :", battery.percent)
print("Power plugged in :", battery.power_plugged)



# system battery check code

import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print("Battery Percentage:", battery.percent)
    print("Power plugged in:", battery.power_plugged)
else:
    print("No battery found on this system.")


