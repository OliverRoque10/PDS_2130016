import numpy as np
import matplotlib.pyplot as plt

def signals3(des_amp, des_freq, des_phas):
    A = float(des_amp)
    f = float(des_freq)
    phi = float(des_phas)
    Ts = 0.01
    t = np.linspace(-1, 5, 1000)
    n = np.arange(-1, 5, Ts)
    x_continue = A * np.sin(2 * np.pi * f * t + phi)
    x_discrete = A * np.sin(2 * np.pi * f * n + phi)

    # Reference singal
    Ar = 1
    fr = 1
    phir = 0
    xr_continue = Ar * np.sin(2 * np.pi * fr * t + phir)
    xr_discrete = Ar * np.sin(2 * np.pi * fr * n + phir)

    plt.figure(figsize=(8, 8))
    plt.suptitle(f'Our signal (red):      A = {A}, F = {f} Hz, ϕ = {phi} rad\n' +
                 f'Reference signal (black) A = {Ar}, F = {fr} Hz, ϕ = {phir} rad'
                 )

    # Continuous signal
    plt.subplot(3, 1, 1)
    plt.plot(t, xr_continue, 'k--', label='Reference')
    plt.plot(t, x_continue, 'r', label='Continuous')
    plt.title('Continuous Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    # Discrete signal
    plt.subplot(3, 1, 2)
    plt.stem(n, xr_discrete, linefmt='k--', markerfmt='ko', basefmt='k--', label='Reference')
    plt.stem(n, x_discrete, linefmt='r-', markerfmt='ro', basefmt='r-', label='Discrete')
    plt.title('Discrete Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    # Overlapping signals
    plt.subplot(3, 1, 3)
    plt.plot(t, xr_continue, 'k--', label='Continuous reference')
    plt.stem(n, xr_discrete, linefmt='k--', markerfmt='ko', basefmt='k--', label='Discrete reference')
    plt.plot(t, x_continue, 'r', label='Continuous')
    plt.stem(n, x_discrete, linefmt='r-', markerfmt='ro', basefmt='r-', label='Discrete')
    plt.title('Overlapping Signals')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
