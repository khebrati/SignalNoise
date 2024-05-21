import sympy as sp
from sympy import symbols, floor
import matplotlib.pyplot as plt

def signal(V, frequency):
    t = symbols('t')
    signal = V * (-1)**floor(2*frequency*t)
    return signal

