import numpy as np
import matplotlib.pyplot as plt

from ber import getBerSamples


period_count = 10
total_points = 200 * period_count
frequency = 1e6
mean_value = 0
standard_deviation = 1
# from 0.1 to 0.3 takes : 5 min
v_values = np.arange(0.1, 2.1, 0.1)
bandwidth = float('inf')
signal_t_points = np.linspace(0, period_count/frequency, total_points).tolist()



ber_values = getBerSamples(period_count, frequency, mean_value, standard_deviation, v_values, bandwidth, signal_t_points)

plt.plot(v_values, ber_values)
plt.xlabel('Volage value')
plt.ylabel('BER')
plt.title('BER for different signal values')
plt.grid(True)
plt.show()