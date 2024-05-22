import matplotlib.pyplot as plt
import numpy as np
from my_signal import signal

frequency = 10e6

signal_t_points = np.linspace(0, 10/frequency, 2000)
signal_values = [signal(v = 5,frequency=frequency).subs('t', t_val) for t_val in signal_t_points]


plt.figure(figsize=(10, 6))
plt.plot(signal_t_points, signal_values)
plt.title('Digital Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()