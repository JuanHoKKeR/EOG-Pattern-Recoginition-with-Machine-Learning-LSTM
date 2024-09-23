import serial
import pandas as pd
import time
import os

# Configuración de la conexión serial
ser = serial.Serial('COM26', 115200)  # Cambiar 'COM3' por tu puerto
ser.flushInput()

# Mapeo de letras a nombres de archivo y contadores para cada tipo de movimiento
file_names = {'R': 'RIGHT.csv', 'L': 'LEFT.csv', 'U': 'UP.csv', 'D': 'DOWN.csv', 'P': 'PRESS.csv'}
data_counters = {key: 0 for key in file_names.keys()}

# Función para cargar o crear el contador de datos
def load_data_counter(file_name):
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
        if not df.empty:
            return df['label'].max() + 1
    return 1

# Cargar o inicializar contadores
for letter, file_name in file_names.items():
    data_counters[letter] = load_data_counter(file_name)

def store_data(label, file_name, counter):
    data_list = []
    start_time = time.time()
    while time.time() - start_time < 2:  # Almacenar datos durante 2 segundos
        if ser.in_waiting > 0:
            try:
                serial_string = ser.readline().decode('utf-8').rstrip()
                horizontal, vertical = map(float, serial_string.split(','))
                data_list.append({'horizontal': horizontal, 'vertical': vertical, 'label': counter})
            except ValueError:
                continue  # Ignorar datos mal formateados
    return data_list

# Bucle principal
while True:
    input_char = input("Ingrese un carácter (R, L, U, D, P) o 'Q' para salir: ").upper()
    if input_char == 'Q':
        print("Saliendo...")
        break
    elif input_char in file_names:
        file_name = file_names[input_char]
        counter = data_counters[input_char]
        data = store_data(counter, file_name, counter)
        data_df = pd.DataFrame(data)
        if os.path.exists(file_name):
            data_df.to_csv(file_name, mode='a', header=False, index=False)
        else:
            data_df.to_csv(file_name, index=False)
        data_counters[input_char] += 1
        print(f"Datos almacenados para {file_name}, sesión {counter}")