import matplotlib.pyplot as plt
import numpy as np
from my_signal import getSignalValues, signal

period_count = 10
# number of points (2000 here) must be divided by period_count
total_points = 200 * period_count
frequency = 1e6
v = 5
signal_t_points = np.linspace(0, period_count/frequency, total_points).tolist()
signal_values = getSignalValues(v,frequency,signal_t_points)


plt.figure(figsize=(10, 6))
plt.plot(signal_t_points, signal_values)
plt.title('Digital Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()