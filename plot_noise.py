import matplotlib.pyplot as plt
import numpy as np
from my_signal import signal
from my_noise import normal_distributed_noise

mean_value = 0
standard_devation = 1

t_values = np.linspace(-5, 5, 1000)
signal_values = [normal_distributed_noise(mean_value, standard_devation).subs('t', t_val) for t_val in t_values]


plt.figure(figsize=(10, 6))
plt.plot(t_values, signal_values)
plt.title('Digital Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()