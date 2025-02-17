import numpy as np
import matplotlib.pyplot as plt

thrust = 9.8
time_duration = 100

time_steps = np.linspace(0, time_duration, 100)

altitude = 0.5*thrust*time_steps**2

plt.figure(figsize=(8,5))

plt.plot(time_steps, altitude, label="Rocket altitude", color = "red", linewidth=2)
plt.title("ROcket altitude VS time ")
plt.xlabel("Time (seconds)")
plt.ylabel("Altitude (meters)")
plt.legend()
plt.show()
