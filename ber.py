import math

import numpy as np

from my_channel import channel
from my_signal import signal
def getSamplingPoints(signal_t_points :list, period_count : int):
    points_in_period = len(signal_t_points) / period_count
    index = int(math.ceil(points_in_period)/4)
    sampling_points = []
    while index < len(signal_t_points):
        sampling_points.append(index)
        index = int(index + points_in_period/2)

    return sampling_points


def ber(signal_t_points : list,signal_values : list,noised_signal : list,period_count : int):
    if len(signal_t_points) != len(signal_values):
        raise ValueError
    error_count = 0
    sampling_points = getSamplingPoints(signal_t_points,period_count)
    print("we have ",len(sampling_points),"sample points")
    for s in sampling_points:
        print("signal has value", signal_values[s], "and noised signal has value ", noised_signal[s])
        if(signal_values[s] > 0): # logical one (= v)
            if(noised_signal[s] < 0):
                error_count += 1
        elif(signal_values[s] < 0):
            if(noised_signal[s] > 0):
                error_count += 1
        print("error count is ",error_count)                     
            
    return error_count/len(sampling_points)



period_count = 10
# number of points (2000 here) must be divided by period_count
total_points = 2000
frequency = 1e6
signal_t_points = np.linspace(0, period_count/frequency, total_points).tolist()
signal_values = [signal(v = 1,frequency=frequency).subs('t', t_val) for t_val in signal_t_points]
print(ber(signal_t_points,signal_values,channel(signal_t_points,2,frequency,0,1),period_count))
