import math

import numpy as np
def getSamplingPoints(signal_t_points :list, period_count : int):
    points_in_period = len(signal_t_points) / period_count
    index = int(math.ceil(points_in_period)/4)
    sampling_points = []
    while index < len(signal_t_points):
        print(index)
        sampling_points.append(index)
        index = index + points_in_period

    return sampling_points

period_count = 10
frequency = 1e6
# number of points (2000 here) must be divided by 10 (qoutient of frequency)
signal_t_points = np.linspace(0, period_count/frequency, 2000).tolist()
print(getSamplingPoints(signal_t_points,period_count))