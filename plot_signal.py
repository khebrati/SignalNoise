import matplotlib.pyplot as plt
import numpy as np
from my_signal import signal



t_values = np.linspace(0, 10e-6, 1000) 
signal_values = [signal().subs('t', t_val) for t_val in t_values]


plt.figure(figsize=(10, 6))
plt.plot(t_values, signal_values)
plt.title('Digital Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()