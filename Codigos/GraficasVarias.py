import pandas as pd
import matplotlib.pyplot as plt

def graficar_sesion(data_df, sesion):
    # Filtrar los datos para la sesión específica
    sesion_df = data_df[data_df['label'] == sesion]

    # Verificar si hay datos para graficar
    if sesion_df.empty:
        print(f"No se encontraron datos para la sesión {sesion}")
        return False

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(sesion_df['horizontal'], label='Horizontal')
    plt.plot(sesion_df['vertical'], label='Vertical')
    plt.title(f'Gráfica de la sesión {sesion}')
    plt.xlabel('Muestra')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()
    return True

def eliminar_sesion(data_df, sesion, archivo):
    # Eliminar los datos de la sesión específica
    data_df = data_df[data_df['label'] != sesion]
    # Guardar el DataFrame actualizado
    data_df.to_csv(archivo, index=False)
    print(f"Sesión {sesion} eliminada del archivo {archivo}.")

def menu():
    archivo = input("Ingrese el nombre del archivo CSV (por ejemplo, 'RIGHT.csv'): ")
    data_df = pd.read_csv(archivo)

    while True:
        print("\nMenú:")
        print("1. Graficar una sesión")
        print("2. Eliminar una sesión")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            sesion = int(input("Ingrese el número de la sesión para graficar: "))
            graficar_sesion(data_df, sesion)
        elif opcion == '2':
            sesion = int(input("Ingrese el número de la sesión para eliminar: "))
            eliminar_sesion(data_df, sesion, archivo)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()