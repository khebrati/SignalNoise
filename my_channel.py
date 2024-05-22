from my_signal import signal
from noise_generator import generate_noise
import numpy as np
import sympy as sp
import math

def channel(signal_x_points,v, frequency, mean_value, standard_devation):
    t = sp.symbols('t')
    signal_expr = signal(v, frequency)
    signal_values = [signal_expr.subs(t, t_val) for t_val in signal_x_points]
    noise_values = generate_noise(mean_value, standard_devation, len(signal_x_points))
    return [s + n for s, n in zip(signal_values, noise_values)]