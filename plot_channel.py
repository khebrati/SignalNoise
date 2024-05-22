import matplotlib.pyplot as plt
import numpy as np
from my_channel import channel

frequency = 1e6
# number of points (2000 here) must be divided by 10 (qoutient of frequency)
signal_t_points = np.linspace(0, 2/frequency, 2000)


channel_values = channel(mean_value=0,standard_devation= 1,v=2,frequency=frequency,signal_x_points= signal_t_points)


plt.figure(figsize=(10, 6))
plt.plot(signal_t_points, channel_values)
plt.title('Channel Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()