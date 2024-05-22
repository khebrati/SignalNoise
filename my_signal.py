import sympy as sp
from sympy import symbols, floor
import matplotlib.pyplot as plt

def signal(v, frequency):
    t = symbols('t')
    signal = v * (-1)**floor(2*frequency*t)
    return signal

