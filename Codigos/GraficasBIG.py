import pandas as pd
import matplotlib.pyplot as plt

def graficar_sesiones(archivo, sesiones):
    # Cargar los datos
    data_df = pd.read_csv(archivo)

    # Crear la figura y los ejes para los subplots
    fig, axs = plt.subplots(len(sesiones), 1, figsize=(10, 6*len(sesiones)))

    for i, sesion in enumerate(sesiones):
        # Filtrar los datos para la sesión específica
        sesion_df = data_df[data_df['label'] == sesion]

        # Verificar si hay datos para graficar
        if sesion_df.empty:
            print(f"No se encontraron datos para la sesión {sesion} en el archivo {archivo}")
            continue

        # Crear la gráfica en el subplot correspondiente
        axs[i].plot(sesion_df['vertical'], sesion_df['horizontal'], 'o', label='Etiqueta')
        axs[i].set_title(f'Gráfica de la sesión {sesion} en {archivo}')
        axs[i].set_xlabel('Muestra')
        axs[i].set_ylabel('Valor')
        axs[i].legend()

    # Ajustar el espacio entre los subplots
    plt.tight_layout()
    plt.show()

# Ejemplo de uso
archivo = 'RIGHT.csv'  # Cambiar por el nombre del archivo correspondiente
sesiones = [2, 5, 10, 15, 22, 27, 30, 36, 40, 47]  # Cambiar por los números de las sesiones que quieres graficar
graficar_sesiones(archivo, sesiones)