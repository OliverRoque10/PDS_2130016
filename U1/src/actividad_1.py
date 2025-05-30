import numpy as np
import matplotlib.pyplot as plt


#señales
def sin(t, f=2):
    return np.sin(2 * np.pi * f * t)

def expostep(t):
    return np.exp(-2 * t) * (t >= 0).astype(float)

def trian(t, f=2):
    T = 1 / f
    t_mod = np.mod(t, T)
    return 4 * np.abs(t_mod / T - 0.5) - 1

def cuad(t, f=2):
    T = 1 / f
    t_mod = np.mod(t, T)
    return np.where(t_mod < T/2, 1, -1)

#graficas
def graphs(t_cont, x_cont, t_disc, x_disc, title):
    plt.figure(figsize=(8, 8))

    plt.subplot(3, 1, 1)
    plt.plot(t_cont, x_cont, 'yellow')
    plt.title(f'{title} - Señal Continua')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.stem(t_disc, x_disc, basefmt="r")
    plt.title(f'{title} - Señal Discreta')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t_cont, x_cont, 'yellow', label="Señal Continua")
    plt.stem(t_disc, x_disc, basefmt="r", label="Señal Discreta")
    plt.title(f'{title} - Ambas Señales')
    plt.grid()

    plt.tight_layout()
    plt.show()

#definir actividad
def actividad_1():
    t_cont = np.linspace(-1, 5, 1000)
    Ts = 0.025
    t_disc = np.arange(-1, 5 + Ts, Ts)

    signals = {
        "Senoidal": sin,
        "Exponencial y escalon": expostep,
        "Traingular": trian,
        "Cuadrada": cuad
    }

    for title, func in signals.items():
        x_cont = func(t_cont)
        x_disc = func(t_disc)
        graphs(t_cont, x_cont, t_disc, x_disc, title)
