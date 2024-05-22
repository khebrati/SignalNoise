import numpy as np

def generate_noise(mean, std_dev, size):
    return np.random.normal(mean, std_dev, size)
