import numpy as np
import matplotlib.pyplot as plt

lookup_dict = {"frequency": {"fast": 9, "slow": 1}}

def run(amplitude, frequency):
    """Deterimne if the maximum value of the sine function equals ``amplitude``"""
    x = np.arange(0, 10, .05)
    y = amplitude * np.sin(frequency * x)
    err = np.abs(max(y) - amplitude)
    plt.plot(x, y)
    return {"main": err}
