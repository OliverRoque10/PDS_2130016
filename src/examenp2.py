import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def dft2():
    # -----------------------------
    # Parámetros de la señal
    # -----------------------------
    fs = 256            # Frecuencia de muestreo
    Ts = 1 / fs         # Periodo de muestreo
    duration = 6        # Duración en segundos
    N = int(fs * duration)  # Número de muestras
    n = np.arange(N)    # Índices de las muestras

    # Frecuencias de la señal
    f1 = 8
    f2 = 20

    # -----------------------------
    # Señal original
    # -----------------------------
    x_n = np.sin(2 * np.pi * f1 * n * Ts) + 0.5 * np.sin(2 * np.pi * f2 * n * Ts)

    # Graficar señal original
    continuous_plotter(n * Ts, x_n, "Señal Original", "x[n]", "Tiempo [s]", "Amplitud")

    # -----------------------------
    # Añadir ruido
    # -----------------------------
    f_noise = 50
    noise = 0.5 * np.sin(2 * np.pi * f_noise * n * Ts)  # Ruido senoidal
    x_n_noise = x_n + noise

    # Graficar señal con ruido
    continuous_plotter(n * Ts, x_n_noise, "Señal con Ruido", "x[n]+ruido", "Tiempo [s]", "Amplitud")

    # -----------------------------
    # DFT de la señal original
    # -----------------------------
    X = np.fft.fft(x_n)
    X_noise = np.fft.fft(x_n_noise)
    freqs = np.fft.fftfreq(N, Ts)
    half = N // 2  # Mitad positiva

    # Graficar DFT señal original
    discrete_plotter(freqs[:half], np.abs(X[:half]), "DFT Señal Original", "Amplitud DFT", "Frecuencia [Hz]", "Amplitud")

    # Graficar DFT señal con ruido
    discrete_plotter(freqs[:half], np.abs(X_noise[:half]), "DFT Señal con Ruido", "Amplitud DFT", "Frecuencia [Hz]", "Amplitud")

    # -----------------------------
    # Resolución de frecuencia
    # -----------------------------
    delta_f = fs / N
    print(f"Resolución de frecuencia Δf = {delta_f:.4f} Hz")
