import sympy as sp
from sympy import symbols, floor
from itertools import repeat
import matplotlib.pyplot as plt

def signal(v, frequency,bandwidth):
    t = symbols('t')
    signal = 0

    if(bandwidth == float('inf')):
        signal = v * (-1)**floor(2*frequency*t)
        return signal
    k = 1
    for i in range(1,2 * bandwidth + 1):
        signal += 1/k * sp.sin(2*sp.pi*k*frequency*t)
        k += 2
    return 4/sp.pi * signal

def getSignalValues(v,frequency,signal_t_points,bandwidth):
    return [signal(v,frequency,bandwidth).subs('t', t_val) for t_val in signal_t_points]

