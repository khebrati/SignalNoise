from sympy import symbols
import sympy as sp

def normal_distributed_noise(mean = 0, std_dev = 1):
    t = symbols('t')
    expr = (1 / (std_dev * sp.sqrt(2 * sp.pi))) * sp.exp(-1/2 * ((t - mean) / ( std_dev))**2)
    return expr