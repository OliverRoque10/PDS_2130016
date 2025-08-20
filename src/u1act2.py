import numpy as np
from src.utils.grapher import signal_graphs

def signals2(des_freq):
    f = float(des_freq)
    A = 1
    Ts = 0.01
    t = np.linspace(-1, 5, 1000)
    tn = np.arange(-1, 5, Ts)
    x1_continue = A * np.sin(2 * np.pi * f * t)
    x1_discrete = A * np.sin(2 * np.pi * f * tn)

    signal_graphs(t, tn, x1_continue, x1_discrete, 'Sinusoidal')
