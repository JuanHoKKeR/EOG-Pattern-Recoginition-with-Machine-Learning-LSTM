import pandas as pd
import matplotlib.pyplot as plt

def graficar_sesion(archivo, sesion):
    # Cargar los datos
    data_df = pd.read_csv(archivo)

    # Filtrar los datos para la sesión específica
    sesion_df = data_df[data_df['label'] == sesion]

    # Verificar si hay datos para graficar
    if sesion_df.empty:
        print(f"No se encontraron datos para la sesión {sesion} en el archivo {archivo}")
        return

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    #plt.plot(sesion_df['horizontal'], label='Horizontal')
    #plt.plot(sesion_df['vertical'], label='Vertical')
    plt.plot(sesion_df['vertical'], sesion_df['horizontal'], 'o', label='Etiqueta')
    
    plt.title(f'Gráfica de la sesión {sesion} en {archivo}')
    plt.xlabel('Muestra')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()

# Ejemplo de uso
archivo = 'RIGHT.csv'  # Cambiar por el nombre del archivo correspondiente
sesion = 31  # Cambiar por el número de sesión que quieres graficar
graficar_sesion(archivo, sesion)