import numpy as np
from src import signal_graphs

def senales_senoidales(frecuencia_deseada):
    frecuencia = float(frecuencia_deseada)
    amplitud = 1
    periodo_muestreo = 0.01
    tiempo_continuo = np.linspace(-1, 5, 1000)
    tiempo_discreto = np.arange(-1, 5, periodo_muestreo)
    
    senal_continua = amplitud * np.sin(2 * np.pi * frecuencia * tiempo_continuo)
    senal_discreta = amplitud * np.sin(2 * np.pi * frecuencia * tiempo_discreto)

    signal_graphs(
        tiempo_continuo,
        tiempo_discreto,
        senal_continua,
        senal_discreta,
        'Señal Senoidal'
    )
