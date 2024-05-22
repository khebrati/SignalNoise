from my_signal import signal
from noise_generator import generate_noise
import numpy as np
import sympy as sp
import math

def channel(signal_values,signal_t_points, mean_value, standard_devation):
    noise_values = generate_noise(mean_value, standard_devation, len(signal_t_points))
    return [s + n for s, n in zip(signal_values, noise_values)]