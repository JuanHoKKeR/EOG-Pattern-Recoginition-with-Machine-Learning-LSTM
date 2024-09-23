import os
import pandas as pd

# Directorio donde se encuentran tus archivos CSV
directory = r'C:\Users\Asus\Documents\aUniversidad\SEMESTRE 23-2\Bio_I\Proyecto'

# Mapeo de letras a nombres de archivo y contadores para cada tipo de movimiento
file_names = {'R': 'RIGHT_.csv', 'L': 'LEFT_.csv', 'U': 'UP_.csv', 'D': 'DOWN_.csv', 'P': 'PRESS_.csv'}

# Recorrer cada archivo y agregar una columna con el tipo de movimiento
for letter, file_name in file_names.items():
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        # Leer el archivo CSV existente
        data_df = pd.read_csv(file_path)
        
        # Agregar una columna con el tipo de movimiento
        data_df['movement_type'] = letter
        
        # Guardar los datos actualizados en el mismo archivo CSV
        data_df.to_csv(file_path, index=False)

        print(f"Columna 'movement_type' agregada a {file_name}")
    else:
        print(f"Archivo {file_name} no encontrado en el directorio especificado.")

print("Proceso completado.")
