import matplotlib.pyplot as plt
import numpy as np
from my_channel import channel
from my_signal import getSignalValues, signal

period_count = 10
# number of points (2000 here) must be divided by period_count
total_points = 200 * period_count
frequency = 1e6
v = 5
bandwidth = float('inf')
mean_value = 0
standard_deviation = 1
signal_t_points = np.linspace(0, period_count/frequency, total_points).tolist()
signal_values = getSignalValues(v,frequency,signal_t_points,bandwidth)


channel_values = channel(signal_values,signal_t_points,mean_value,standard_deviation)


plt.figure(figsize=(10, 6))
plt.plot(signal_t_points, channel_values)
plt.title('Channel Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()