import numpy as np
from src.utils.grapher import dac_graphs

def dac_bits(def_bits):
    N = int(def_bits)
    VFS = 5.0
    lev = 2 ** N

    step_size = VFS / (lev - 1)
    resolution_pct = (step_size / VFS) * 100

    digital_input = np.arange(lev)
    analog_output = digital_input * step_size

    print(f"Bits: {N}")
    print(f"Levels: {lev} (0 to {lev - 1})")
    print(f"Step size: {step_size:.6f} V/step")
    print(f"Resolution(% VFS): {resolution_pct:.6f}%")
    print(f"Voltage full scale: {VFS} V")

    dac_graphs(digital_input, analog_output, VFS, lev, N)
