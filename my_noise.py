from sympy import symbols
import sympy as sp

def normal_distribution(mean, std_dev):
    t = symbols('t')
    expr = (1 / (std_dev * sp.sqrt(2 * sp.pi))) * sp.exp(-1/2 * ((t - mean) / ( std_dev))**2)
    return expr