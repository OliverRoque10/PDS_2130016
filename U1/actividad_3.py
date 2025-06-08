import numpy as np
import matplotlib.pyplot as plt

def representar_senales(amplitud, frecuencia, fase):
    # Conversión a flotante
    A = float(amplitud)
    f = float(frecuencia)
    phi = float(fase)

    # Parámetros de tiempo
    paso_muestreo = 0.01
    tiempo_continuo = np.linspace(-1, 5, 1000)
    tiempo_discreto = np.arange(-1, 5, paso_muestreo)

    # Señales generadas
    senal_continua = A * np.sin(2 * np.pi * f * tiempo_continuo + phi)
    senal_discreta = A * np.sin(2 * np.pi * f * tiempo_discreto + phi)

    # Señal de referencia
    A_ref = 1
    f_ref = 1
    phi_ref = 0
    senal_continua_ref = A_ref * np.sin(2 * np.pi * f_ref * tiempo_continuo + phi_ref)
    senal_discreta_ref = A_ref * np.sin(2 * np.pi * f_ref * tiempo_discreto + phi_ref)

    # Gráfica
    plt.figure(figsize=(10, 9))
    plt.suptitle(
        f'Señal generada (roja): A = {A}, f = {f} Hz, ϕ = {phi} rad\n' +
        f'Señal de referencia (negra): A = {A_ref}, f = {f_ref} Hz, ϕ = {phi_ref} rad'
    )

    # Gráfico continuo
    plt.subplot(3, 1, 1)
    plt.plot(tiempo_continuo, senal_continua_ref, 'k--', label='Referencia continua')
    plt.plot(tiempo_continuo, senal_continua, 'r', label='Señal continua')
    plt.title('Señal en Tiempo Continuo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid()

    # Gráfico discreto
    plt.subplot(3, 1, 2)
    plt.stem(tiempo_discreto, senal_discreta_ref, linefmt='k--', markerfmt='ko', basefmt='k--', label='Referencia discreta')
    plt.stem(tiempo_discreto, senal_discreta, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal discreta')
    plt.title('Señal en Tiempo Discreto')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid()

    # Gráfico combinado
    plt.subplot(3, 1, 3)
    plt.plot(tiempo_continuo, senal_continua_ref, 'k--', label='Referencia continua')
    plt.stem(tiempo_discreto, senal_discreta_ref, linefmt='k--', markerfmt='ko', basefmt='k--', label='Referencia discreta')
    plt.plot(tiempo_continuo, senal_continua, 'r', label='Señal continua')
    plt.stem(tiempo_discreto, senal_discreta, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal discreta')
    plt.title('Señales Superpuestas')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid()

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.show()
