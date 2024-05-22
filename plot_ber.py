from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from my_channel import channel
from my_signal import getSignalValues
from ber import ber

period_count = 10
total_points = 200 * period_count
frequency = 1e6
mean_value = 0
standard_deviation = 1

v_values = np.arange(0.1, 2.1, 0.1)
ber_values = []
signal_t_points = np.linspace(0, period_count/frequency, total_points).tolist()

for v in v_values:
    signal_values = getSignalValues(v, frequency, signal_t_points)
    ber_value = ber(signal_t_points, signal_values, channel(signal_values, signal_t_points, mean_value, standard_deviation), period_count)
    ber_values.append(ber_value)

plt.plot(v_values, ber_values)
plt.xlabel('Volage value')
plt.ylabel('BER')
plt.title('BER for different signal values')
plt.grid(True)
plt.show()