import numpy as np
from scipy import signal
from src.utils.grapher import signal_graphs

def signals1():
    
    f = 2 # Frec
    t = np.linspace(-1, 5, 1000)
    Ts = 0.05 # Sampling P
    tn = np.arange(-1, 5, Ts)
    # Sin
    x1_continue = np.sin(2 * np.pi * f * t)
    x1_discrete = np.sin(2 * np.pi * f * tn)
    # ExpUS
    u = np.heaviside(t, 1)
    x2_continue = np.exp(-2 * t) * u
    u_discrete = np.heaviside(tn, 1)
    x2_discrete = np.exp(-2 * tn) * u_discrete
    # Tria
    x3_continue = signal.sawtooth(2 * np.pi * f * t, width=0.5)
    x3_discrete = signal.sawtooth(2 * np.pi * f * tn, width=0.5)
    # Squa
    x4_continue = signal.square(2 * np.pi * f * t)
    x4_discrete = signal.square(2 * np.pi * f * tn)

    # Plots
    signal_graphs(t, tn, x1_continue, x1_discrete, 'Sinusoidal')
    signal_graphs(t, tn, x2_continue, x2_discrete, 'Exponential with Unit Step')
    signal_graphs(t, tn, x3_continue, x3_discrete, 'Triangular')
    signal_graphs(t, tn, x4_continue, x4_discrete, 'Square')
